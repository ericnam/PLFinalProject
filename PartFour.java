import java.util.*;
public class PartFour {
        public static void strop() {
            ArrayList<List<Object>> emp = new ArrayList<List<Object>>();
            ArrayList<List<Object>> dept = new ArrayList<List<Object>>();

            List<Object> e1 = Arrays.asList(10, "Jackson", "Marta", "jacksomt", "27-FEB-91", "", "Warehouse Manager", 1507, 0, 45, 2);
            List<Object> e2 = Arrays.asList(11, "Henderson", "Colin", "hendercs", "14-MAY-90", "", "Sales Representative", 1400, 10, 31, 3);
            List<Object> e3 = Arrays.asList(1, "Martin", "Carmen", "martincu", "3-Mar-90", "", "President", 4500, 0, 50, 0);
            List<Object> e4 = Arrays.asList(12, "Gilson", "Sam", "gilsonsj", "18-Jan-92", "", "Sales Representative", 1490, 12.5, 32, 3);
            List<Object> e5 = Arrays.asList(13, "Sanders", "Jason", "sanderjk", "18-Feb-91", "", "Sales Representative", 1515, 10, 33, 3);
            List<Object> e6 = Arrays.asList(14, "Dameron", "Andre", "dameroap", "9-Oct-91", "", "Sales Representative", 1450, 17.5, 35, 3);
            List<Object> e7 = Arrays.asList(15, "Hardwick", "Elaine", "hardwiem", "7-Feb-92", "", "Stock Clerk", 1400, 0, 41, 6);
            List<Object> e8 = Arrays.asList(16, "Brown", "George", "browngw", "8-Mar-90", "", "Stock Clerk", 940, 0, 41, 6);
            List<Object> e9 = Arrays.asList(17, "Washington", "Thomas", "washintl", "9-Feb-91", "", "Stock Clerk", 1200, 0, 42, 7);
            List<Object> e10 = Arrays.asList(18, "Patterson", "Donald", "patterdv", "6-Aug-91", "", "Stock Clerk", 795, 0, 42, 7);
            List<Object> e11 = Arrays.asList(19, "Bell", "Alexander", "bellag", "26-May-91", "", "Stock Clerk", 850, 0, 43, 8);
            List<Object> e12 = Arrays.asList(2, "Smith", "Doris", "smithdj", "8-Mar-90", "", "VP, Operations", 2450, 0, 41, 1);
            List<Object> e13 = Arrays.asList(20, "Gantos", "Eddie", "gantosej", "30-Nov-90", "", "Stock Clerk", 800, 0, 44, 9);
            List<Object> e14 = Arrays.asList(21, "Stephenson", "Blaine", "stephebs", "17-Mar-91", "", "Stock Clerk", 860, 0, 45, 10);
            List<Object> e15 = Arrays.asList(22, "Chester", "Eddie", "chesteek", "30-Nov-90", "", "Stock Clerk", 800, 0, 44, 9);
            List<Object> e16 = Arrays.asList(23, "Pearl", "Roger", "pearlrg", "17-Oct-90", "", "Stock Clerk", 795, 0, 34, 9);
            List<Object> e17 = Arrays.asList(24, "Dancer", "Bonnie", "dancerbw", "17-Mar-91", "", "Stock Clerk", 860, 0, 45, 7);
            List<Object> e18 = Arrays.asList(25, "Schmitt", "Sandra", "schmitss", "9-May-91", "", "Stock Clerk", 1100, 0, 45, 8);
            List<Object> e19 = Arrays.asList(3, "Norton", "Michael", "nortonma", "17-Jun-91", "", "VP, Sales", 2400, 0, 31, 1);
            List<Object> e20 = Arrays.asList(4, "Quentin", "Mark", "quentiml", "7-Apr-90", "", "VP, Finance", 2450, 0, 10, 1);
            List<Object> e21 = Arrays.asList(5, "Roper", "Joseph", "roperjm", "4-Mar-90", "", "VP, Administration", 2550, 0, 50, 1);
            List<Object> e22 = Arrays.asList(6, "Brown", "Molly", "brownmr", "18-Jan-91", "", "Warehouse Manager", 1600, 0, 41, 2);
            List<Object> e23 = Arrays.asList(7, "Hawkins", "Roberta", "hawkinrt", "14-May-90", "", "Warehouse Manager", 1650, 0, 42, 2);
            List<Object> e24 = Arrays.asList(8, "Burns", "Ben", "burnsba", "7-Apr-90", "", "Warehouse Manager", 1500, 0, 43, 2);
            List<Object> e25 = Arrays.asList(9, "Catskill", "Antoinette", "catskiaw", "9-Feb-92", "", "Warehouse Manager", 1700, 0, 44, 2);

            List<Object> d1 = Arrays.asList(10, "Finance", 1);
            List<Object> d2 = Arrays.asList(31, "Sales", 1);
            List<Object> d3 = Arrays.asList(32, "Sales", 2);
            List<Object> d4 = Arrays.asList(33, "Sales", 3);
            List<Object> d5 = Arrays.asList(34, "Sales", 4);
            List<Object> d6 = Arrays.asList(35, "Sales", 5);
            List<Object> d7 = Arrays.asList(41, "Operations", 1);
            List<Object> d8 = Arrays.asList(42, "Operations", 2);
            List<Object> d9 = Arrays.asList(43, "Operations", 3);
            List<Object> d10 = Arrays.asList(44, "Operations", 4);
            List<Object> d11 = Arrays.asList(45, "Operations", 5);
            List<Object> d12 = Arrays.asList(50, "Administration", 1);

            emp.add(e1);emp.add(e2);emp.add(e3);emp.add(e4);emp.add(e5);emp.add(e6);emp.add(e7);emp.add(e8);emp.add(e9);emp.add(e10);emp.add(e11);emp.add(e12);emp.add(e13);emp.add(e14);emp.add(e15);emp.add(e16);emp.add(e17);emp.add(e18);emp.add(e19);emp.add(e20);emp.add(e21);emp.add(e22);emp.add(e23);emp.add(e24);emp.add(e25);
            dept.add(d1);dept.add(d2);dept.add(d3);dept.add(d4);dept.add(d5);dept.add(d6);dept.add(d7);dept.add(d8);dept.add(d9);dept.add(d10);dept.add(d11);dept.add(d12);

            System.out.println("select last_name, first_name, title, salary, name from s_emp e join s_dept d on(e.dept_id = d.id): ");
            emp.stream()
                    .flatMap(e -> dept.stream()
                            .filter(d -> Objects.equals(e.get(9), d.get(0)))
                            .map(d -> Arrays.asList(e.get(1), e.get(2), e.get(6), e.get(7), d.get(1)))
                    )
                    .forEach(e -> {
                        // should this output be fed into mini-lisp for post processing, or should it be run through all first and then sent to mini-lisp?
                        System.out.println(e);
                    });
            System.out.println();
        }

}