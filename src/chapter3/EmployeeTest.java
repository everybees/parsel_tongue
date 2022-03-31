package chapter3;

public class EmployeeTest {
    public static void main(String[] args) {
        Employee emply = new Employee("Sandra", "Ogunbola", 300_000.0);
        System.out.println("employee one yearly salary is : "+ emply.getYearlySalary());

        Employee emply2 = new Employee("Gideon", "Udoh", 250_000.0);
        System.out.println("employee two yearly salary is : " + emply2.getMonthlySalary());

        emply.setPerRaise(10);
        System.out.println("employee 1 salary by 10:" + emply.getYearlySalary());
    }
}
