package credit_calculator;

import java.util.ArrayList;
import java.util.Scanner;

public class CreditLimitApplication {
    private static double monthlyAllowedCreditLimit = 500.00;

    private static ArrayList<Item> items= new ArrayList<>();
    public static void main(String[] args) {
        double total = 0;
        Scanner input = new Scanner(System.in);
        while (total <= monthlyAllowedCreditLimit){
            System.out.println("Enter name of Item");
            String itemName = input.nextLine();
            System.out.println("Enter price of Item");
            double itemPrice = input.nextDouble();
            input.nextLine();
            Item item = new Item(itemName, itemPrice);
            items.add(item);
            total += itemPrice;
        }
        for(Item item : items){
            System.out.println(item);
        }
        System.out.printf("Total credit = "+total);

    }
}
