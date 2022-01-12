package chapter4;

import java.util.Scanner;

public class BinaryToDecimal {
    //Ask user to enter a binary number
    //convert a binary number to decimal
    //print out a decimal number
    public static void main(String[] args) {
        int decimal = 0;
        int binary ;
        int reminder;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a Binary Number");
        binary = input.nextInt();

        while(binary > 0) {
            reminder = binary % 10;
            binary = binary / 10;
            decimal = decimal * 10 + reminder;
        }
        System.out.println("Decimal number: ");
    }
}
