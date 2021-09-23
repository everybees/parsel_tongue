package chapter4;

import java.util.Scanner;

public class Loop_list {
    public static void main(String[] args) {
        int sum =0;
        int score=0;
        double avg =0;

        Scanner input = new Scanner(System.in);

        for (int count = 1; count <= 2; count = count + 1) {
            System.out.print("Enter a Score " + count+ ":");

            score = input.nextInt();
            sum = sum + score;
            avg = (double) sum / count;

          //  System.out.println(sum+ "");
        }
        }
       //System.out.println(avg + "");
     //  System.out.println(sum+ " ");


    }

