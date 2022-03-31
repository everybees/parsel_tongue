package chapter4;

import java.util.Scanner;

public class CreditLimitCalculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your account Number: ");
        int accountNumber = input.nextInt();
        System.out.println("Enter the beginning balance of the month: ");
        int balanceBeginOfTheMonth = input.nextInt();
        System.out.println("Enter the total item of the customer for the month: ");
        int totalChargeForItemForTheMonth = input.nextInt();
        System.out.println("Enter the total credit of the customer for the month: ");
        int totalCreditForTheMonth = input.nextInt();
        System.out.println("Enter the credit limit: ");
        int creditLimit = input.nextInt();

        int newBalance = balanceBeginOfTheMonth + totalChargeForItemForTheMonth - totalCreditForTheMonth;
        System.out.println("This is the new balance: " + newBalance);

        if (newBalance > creditLimit){
            System.out.println("Credit limit exceeded");
        }
    }

}
