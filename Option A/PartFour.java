import java.util.*;
public class PartFour {
        public static String strop() {
            ArrayList<List<Object>> emp = new ArrayList<List<Object>>();
            Scanner reader = new Scanner(System.in);
            String loop = "y";
            while (loop.equals("y")) {
                System.out.println("Please input last name: ");
                String last_name = reader.next();

                System.out.println("Please input first name: ");
                String first_name = reader.next();

                System.out.println("Please input monthly salary: ");
                int salary = reader.nextInt();

                System.out.println("Please input position: ");
                String position = reader.next();

                List<Object> e1 = Arrays.asList(last_name, first_name, salary, position);
                emp.add(e1);

                System.out.println("Input another employee? (y/n)");
                loop = reader.next();
            }

            // System.out.println(emp);

            // System.out.println("Program will now output employee Last Name and Yearly Salary:");
            StringBuilder sb = new StringBuilder();
            emp.stream()
                    .filter(e -> ((Number) e.get(2)).intValue() > 1200)
                    .map(e -> Arrays.asList(e.get(0), e.get(2)))
                    .forEach(e -> {
                        sb.append(e);
                        sb.append("\n");
                    });
            // System.out.println(sb.toString());
            return sb.toString();
        }

}