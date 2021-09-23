package chapter4;

import org.w3c.dom.ls.LSOutput;

import java.util.Scanner;

public class SalesCommissionCalculator {
    public static void main(String[] args) {
        Scanner sales = new Scanner(System.in);
        System.out.println("Enter sales person's item sold in a week");
        int saleSoldInLastWeek = sales.nextInt();

        double commission = 90/100 * saleSoldInLastWeek;

    }
}