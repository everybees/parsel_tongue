package chapter11;

import java.util.InputMismatchException;
import java.util.Scanner;

public class DivideByZero {
    public static void main(String[] args) throws Exception {
        int firstNumber = input("Enter first number");
        int secondNumber = input("Enter second number");
        //int throwthrow = throwsThrows();

        callThrowThrows();
        try {
            System.out.printf("The quotient is %d", (firstNumber / secondNumber));
        }
        catch (ArithmeticException adesuwa){
            System.out.println("An error occurred");
            System.out.println(adesuwa.getMessage());
        }
    }
    private static void callThrowThrows() throws Exception{
      //  try {
        throwsThrows();
    //}
      //  catch (Exception ex){
          //  System.out.println("HEY MONKEY");
      //  }
    }
    private static int input(String prompt) {
        Scanner scanner = new Scanner(System.in);
        System.out.println(prompt);
        try {
            return scanner.nextInt();
        }
       catch (InputMismatchException ex) {
           System.err.println("mugu");
          // System.out.println("Re-enter mumu");
           return input(prompt);
       }
    }
    private static  int throwsThrows() throws  Exception{
        System.out.println("THrow was called");
      //   throw new Exception("You forced my hands...");
        throw new Error("you crazy fuck up man");
      //  return 50;
    }
}
