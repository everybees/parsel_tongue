package chapter4;

import java.util.Scanner;

public class SalaryCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter list of Employee: ");
        int employee = input.nextInt();
        System.out.println("Enter Number of hours worked last week: ");
        int hoursWorked = input.nextInt();
        System.out.println("Enter their hourly rate: ");
        double hourlyRate = input.nextDouble();

        calculateGrossPay(hoursWorked, hourlyRate);
    }
    public static void calculateGrossPay(int hoursWorked, double hourlyRate){
        double grossPay = hoursWorked * hourlyRate;
        System.out.println("The employee grosspay is: " + grossPay);
    }
}
