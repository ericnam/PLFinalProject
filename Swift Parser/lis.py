################ Lispy: Scheme Interpreter in Python

## (c) Peter Norvig, 2010-14; See http://norvig.com/lispy.html

################ Types

from __future__ import division

Symbol = str          # A Lisp Symbol is implemented as a Python str
List   = list         # A Lisp List is implemented as a Python list
Number = (int, float) # A Lisp Number is implemented as a Python int or float

################ Parsing: parse, tokenize, and read_from_tokens

# def parse(program):
#     "Read a Scheme expression from a string."
#     return read_from_tokens(tokenize(program))

# def tokenize(s):
#     "Convert a string into a list of tokens."
#     return s.replace('(',' ( ').replace(')',' ) ').split()

# def read_from_tokens(tokens):
#     "Read an expression from a sequence of tokens."
#     if len(tokens) == 0:
#         raise SyntaxError('unexpected EOF while reading')
#     token = tokens.pop(0)
#     if '(' == token:
#         L = []
#         while tokens[0] != ')':
#             L.append(read_from_tokens(tokens))
#         tokens.pop(0) # pop off ')'
#         return L
#     elif ')' == token:
#         raise SyntaxError('unexpected )')
#     else:
#         return atom(token)

# def atom(token):
#     "Numbers become numbers; every other token is a symbol."
#     try: return int(token)
#     except ValueError:
#         try: return float(token)
#         except ValueError:
#             return Symbol(token)

################ Environments

def standard_env():
    "An environment with some Scheme standard procedures."
    import math, operator as op
    env = Env()
    env.update(vars(math)) # sin, cos, sqrt, pi, ...
    env.update({
        '+':op.add, '-':op.sub, '*':op.mul, '/':op.div, 
        '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, 
        'abs':     abs,
        'append':  op.add,  
        'apply':   apply,
        'begin':   lambda *x: x[-1],
        'car':     lambda x: x[0],
        'cdr':     lambda x: x[1:], 
        'cons':    lambda x,y: [x] + y,
        'eq?':     op.is_, 
        'equal?':  op.eq, 
        'length':  len, 
        'list':    lambda *x: list(x), 
        'list?':   lambda x: isinstance(x,list), 
        'exec':    lambda x: eval(compile(x,'None','single')),
        'map':     map,
        # 'mapp':    lambda x, y: x[0] + y[0],
        'mapp':    lambda y, x: [y(item) for item in x], 
        'max':     max,
        'min':     min,
        'not':     op.not_,
        'null?':   lambda x: x == [], 
        'number?': lambda x: isinstance(x, Number),   
        'run':     lambda x, y: x.run(y[0]) if len(y) < 2 else x.run(y[0])(y[1]),
        'procedure?': callable,
        'round':   round,
        'symbol?': lambda x: isinstance(x, Symbol),
    })
    return env

class Env(dict):
    "An environment: a dict of {'var':val} pairs, with an outer Env."
    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms, args))
        self.outer = outer
    def find(self, var):
        "Find the innermost Env where var appears."
        return self if (var in self) else self.outer.find(var)

global_env = standard_env()

################ Interaction: A REPL

def repl(prompt='lis.py> '):
    "A prompt-read-eval-print loop."
    while True:
        val = eval(parse(raw_input(prompt)))
        if val is not None: 
            print(lispstr(val))

def lispstr(exp):
    "Convert a Python object back into a Lisp-readable string."
    if  isinstance(exp, list):
        return '(' + ' '.join(map(lispstr, exp)) + ')' 
    else:
        return str(exp)

################ Procedures

class Procedure(object):
    "A user-defined Scheme procedure."
    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env
    def __call__(self, *args): 
        return eval(self.body, Env(self.parms, args, self.env))

################ eval

def eval(x, env=global_env):
    "Evaluate an expression in an environment."
    toReturn = None
    if isinstance(x, Symbol):      # variable reference
        try:
            toReturn = env.find(x)[x]
        except:
            # print (__builtins__['eval'])
            try:
                toReturn = __builtins__['eval'](__builtins__['eval'](x))
            except:
                toReturn = x
        # print 'toreturn', toReturn
        # print 'type', type(toReturn)
        return toReturn
    elif not isinstance(x, List):  # constant literal
        return x                
    elif x[0] == 'quote':          # (quote exp)
        (_, exp) = x
        return exp
    elif x[0] == 'if':             # (if test conseq alt)
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif x[0] == 'define':         # (define var exp)
        (_, var, exp) = x
        # print 'exp', exp
        # print 'var', var
        env[var] = eval(exp, env)
    elif x[0] == 'set!':           # (set! var exp)
        (_, var, exp) = x
        env.find(var)[var] = eval(exp, env)
    elif x[0] == 'lambda':         # (lambda (var...) body)
        (_, parms, body) = x
        return Procedure(parms, body, env)
    elif x[0] == 'exec':
        proc = eval(x[0], env)
        # print 'x0', x[0]
        # print 'proc', proc
        import re
        # print 're',re.sub(r"^'|'$", '', x[1])
        exec(proc(re.sub(r"^'|'$", '', x[1])))
        return toReturn
    # elif x[0] == 'run':
        # print env
        # proc = eval(x[0], env)
        # args = [eval(exp, env) for exp in x[1:]]
        # return proc(*x[1:])
    else:                          # (proc arg...)
        proc = eval(x[0], env)
        args = [eval(exp, env) for exp in x[1:]]
        # print 'final', proc, args
        # print 'def final', proc(*args)

        return proc(*args)

# repl()