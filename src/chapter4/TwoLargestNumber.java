package chapter4;

import java.util.Scanner;

public class TwoLargestNumber {
    //Ask user to enter ten numbers
    //Show the two largest number
    public static void main(String[] args) {
        int largest1 = 0;
        int largest2 = 0;

        Scanner input = new Scanner(System.in);
        for (int numbers = 1; numbers <=10; numbers++) {
            System.out.print("Enter numbers " + numbers+ ":");
            int figure= input.nextInt();
            if (figure > largest1) {
                largest2= largest1;
                largest1 = figure;

            }
            else
            if (figure >= largest2) {
                largest2 = largest1 ;

            }
        }
            System.out.println(largest1+ "");
            System.out.println(largest2+ "");
    }
}
