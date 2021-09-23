package chapter4;

import java.util.Scanner;

public class GasMileage {
    public static void main(String[] args) {
        int totalOfMiles = 0;
        int totalOfGallons = 0;
        Scanner input = new Scanner(System.in);
        for (int i = 1; i <= 3; i++) {
            System.out.println("Enter number of miles used: ");
            int miles = input.nextInt();
            totalOfMiles += miles;
            System.out.println("Enter number of gallons used: ");
            int gallons = input.nextInt();
            totalOfGallons += gallons;
            System.out.println("The total of miles is: " + totalOfMiles);
            System.out.println("The total of gallons is: " + totalOfGallons);
        }
        double mileage = totalOfMiles / totalOfGallons;
        System.out.println("The mileage is: " + mileage);
    }
}
