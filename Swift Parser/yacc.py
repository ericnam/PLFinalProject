import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

DEBUG = False

# Namespace & built-in functions

name = {}
var = {}
consts = {}

global ast
ast = []

# Utilities functions
def is_list(l):
    return type(l) == type([])

def lisp_str(l):
    if type(l) == type([]):
        if not l:
            return "()"
        r = "("
        for i in l[:-1]:
            r += lisp_str(i) + " "
        r += lisp_str(l[-1]) + ")"
        return r
    elif l is True:
        return "#t"
    elif l is False:
        return "#f"
    elif l is None:
        return 'nil'
    else:
        return str(l)

# BNF - Backus-Naur Form
def p_print(p):
    'item : PRINT LPAREN item RPAREN'
    try:
        print var[p[3]]
    except:
        try:
            print (consts[p[3]])
        except:
            print "error: use of unresolved identifier '%s'" %p[3]
    
def p_let(p):
    'item : LET item "=" item'
    if (p[2] in consts):
        print "note: '%s' previously declared here"  %p[2]
    else:
        consts[p[2]] = p[4]
    # print var

def p_reassign(p):
    'item : item "=" item'
    if (p[1] not in var and p[1] not in consts):
        print "error: use of unresolved identifier '%s'" %p[1] 
    elif (p[1] in consts):
        print "note: change 'let' to 'var' to make it mutable"
    else:
        var[p[1]] = p[3]

def p_var(p):
    'item : VAR item "=" item'
    var[p[2]] = p[4]

def p_TEXT_item(p):
    'item : TEXT'
    p[0] = p[1]

def p_SIMB_item(p):
    'item : SIMB'
    p[0] = p[1]

def p_NUM_item(p):
    'item : NUM'
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print "Syntax error!! ",p

# Build the parser
# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")
parser = yacc.yacc()

# while True:
#     try:
#         s = raw_input('')
#     except EOFError:
#         break
#     parser.parse(s) 