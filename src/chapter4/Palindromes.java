package chapter4;

import java.util.Scanner;

public class Palindromes {
    //Ask the user to enter a Palindromes of five digit figures
    //Show error, insert five compulsory digit
    //Ask the user to enter another five digit figure
    //if the user enters the right Palindromes
    //display that's a Palindromes number
    //if the user enters the wrong Palindromes
    //display that's not a Palindromes


    public static void main(String[] args) {
        checkForPalindrome();
    }

    private static void checkForPalindrome() {
        //  int number = 0;
        System.out.println("Enter five digit figure" + ":");
        Scanner input = new Scanner(System.in);
        int number = input.nextInt();

        int length = String.valueOf(number).length();

        if (length != 5) {
            System.out.println("Error, insert five compulsory digit");

            checkForPalindrome();

        } else {
            int reminder;
            int reverse = 0;
            int digit = number;

            while (number > 0) {
                reminder = number % 10;
                reverse = reverse * 10 + reminder;
                number = number / 10;
            }

            if (digit == reverse)
                System.out.println("That's a palindromes");
            else {
                System.out.println("That's not a palindromes");
            }
        }
    }


}