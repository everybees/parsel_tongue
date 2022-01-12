package chapter4;

import java.util.Scanner;

public class CreditLimitCalculatorWithMethod2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int accountNumber = 0;
        int balanceBeginOfTheMonth = 0;
        int totalItemOfTheMonth = 0;
        int totalCreditForTheMonth = 0;
        int creditLimit = 0;
        enterAccountNumber(accountNumber);
        balanceAtTheBeginningOfMonth(balanceBeginOfTheMonth);
        totalItemOfTheCustomerForTheMonth(totalCreditForTheMonth);
        totalCreditOfTheCustomerAccountForTheMonth(totalCreditForTheMonth);
        allowedCreditLimit(creditLimit);
        calculateNewBalance(balanceBeginOfTheMonth, totalItemOfTheMonth, totalCreditForTheMonth, creditLimit);
    }
    public static void enterAccountNumber(int accountNumber) {
        System.out.println("Enter your account Number: ");
    }

    public static void balanceAtTheBeginningOfMonth(int balanceBeginOfTheMonth) {
        System.out.println("Enter the beginning balance of the month: ");
    }

    public static void totalItemOfTheCustomerForTheMonth(int totalItemOfTheMonth) {
        System.out.println("Enter the total item of the customer for the month: ");
    }

    public static void totalCreditOfTheCustomerAccountForTheMonth(int totalCreditForTheMonth) {
        System.out.println("Enter the total credit of the customer for the month: ");
    }

    public static void allowedCreditLimit(int creditLimit) {
        System.out.println("Enter the credit limit: ");
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
