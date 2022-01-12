package chapter8;

import java.util.Scanner;

public class NameExchangeReverse {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Whats your name? ");
       String name = input.nextLine();
        for (int i = name.length() - 1; i >= 0; i--) {
            System.out.print(name.charAt(i));
        }
    }
    public static void revee(String name){
        System.out.println(new StringBuilder(name).reverse());
    }
    public static void reverserminc(String love){

    }
}
