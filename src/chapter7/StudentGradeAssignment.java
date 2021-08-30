package chapter7;

import java.util.Scanner;

public class StudentGradeAssignment {
    public static void main(String[] args) {
        int[][] scores;
        Scanner input = new Scanner(System.in);
        System.out.println("How many student do you have? ");
        int numberOfStudent = input.nextInt();
        System.out.println("How many subjects do you do? ");
        int numberOfSubject = input.nextInt();
        scores = new int[numberOfStudent][numberOfSubject];

        for (int row = 0; row < numberOfStudent ; row++) {
            for(int column = 0; column < numberOfSubject; column++){
                System.out.println("Enter scores for student " + (row+1) + " subject " + (column+1) + ": ");
                scores[row][column]= input.nextInt();
            }
        }
        for(int row =0; row < scores.length; row++){
//            scores = new int[numberOfStudent][numberOfSubject];
            System.out.print("Student " + (row+1) + ": ");
            for(int column = 0; column < scores[numberOfSubject].length; column++){
                System.out.print(scores[row][column] + "   ");
            }
            System.out.println();
        }

    }
}
