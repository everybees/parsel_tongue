package chapter6;

import java.util.Scanner;

public class Maximum {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter three numbers: ");
        double number1 = input.nextDouble();
        double number2 = input.nextDouble();
        double number3 = input.nextDouble();
        double result = maximum(number1, number2, number3);
        System.out.println("Maximum is: " + result);
    }

    private static double maximum(double number1, double number2, double number3) {
        double maximumValue = number1;
        if (number2 > maximumValue)
            maximumValue = number2;

        if (number3 > maximumValue)
            maximumValue = number3;

        return maximumValue;
    }
}
