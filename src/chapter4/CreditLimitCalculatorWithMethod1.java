package chapter4;

import java.util.Scanner;

public class CreditLimitCalculatorWithMethod1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your account Number: ");
        int accountNumber = input.nextInt();
        System.out.println("Enter the beginning balance of the month: ");
        int balanceBeginOfTheMonth = input.nextInt();
        System.out.println("Enter the total item of the customer for the month: ");
        int totalItemOfTheMonth = input.nextInt();
        System.out.println("Enter the total credit of the customer for the month: ");
        int totalCreditForTheMonth = input.nextInt();
        System.out.println("Enter the credit limit: ");
        int creditLimit = input.nextInt();

        calculateNewBalance(balanceBeginOfTheMonth, totalItemOfTheMonth, totalCreditForTheMonth, creditLimit);
    }
    public static void calculateNewBalance(int balanceBeginOfTheMonth, int totalItemOfTheMonth, int totalCreditForTheMonth, int creditLimit) {
        int newBalance = balanceBeginOfTheMonth + totalItemOfTheMonth - totalCreditForTheMonth;
        System.out.println("This is the new balance: " + newBalance);

        if (newBalance > creditLimit) {
            System.out.println("Credit limit exceeded");

        } else {
            System.out.println("You are still with your credit limit");
        }
    }
}