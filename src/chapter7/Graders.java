package chapter7;

import java.util.Scanner;

public class Graders {
    public static void main(String[] args) {
        int[][] score;
        Scanner input = new Scanner(System.in);
        System.out.println("How many student? ");
        int student = input.nextInt();
        System.out.println("How many subject? ");
        int subject = input.nextInt();
        score = new int[student][subject];
        int total;
        int highestScore;
        double average;
        for (int row = 0; row < student; row++) {
            for (int column = 0; column < subject; column++) {
                System.out.println("Student " + (row+1) + " Subject " + (column+1) + ":");
                score[row][column] = input.nextInt();
            }
        }
        System.out.print("          ");
        for (int column = 0; column < subject; column++)
            System.out.print(" Subj" + (column+1) + "    ");
        System.out.print("Total");
        System.out.print("  Average");
        System.out.println();

        for (int row = 0; row < student; row++) {
            total = 0;
            average = 0.0;
            System.out.print("Student " + (row+1) + ": ");
            for (int column = 0; column < subject; column++) {
                System.out.printf("%6d", score[row][column]);
                total += score[row][column];
                average = total / subject;
            }
            System.out.printf("%7s", total);
            System.out.printf("%7s", average);
            System.out.println();
        }
//        for (int i = 0; i < score.length; i++) {
//            highestScore = 0;
//            if (score[sub] > highestScore) {
//              highestScore = score[subject];
//            }
        }
    }

