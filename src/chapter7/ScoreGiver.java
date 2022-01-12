package chapter7;

import java.util.Scanner;

public class ScoreGiver<grades> {
    public static int calculateLowestNumber(int[] scores) {
        int lowestScore = scores[0];
        for (int i = 0; i < scores.length; i++)
            if (scores[i] < lowestScore) {
                lowestScore = scores[i];
            }
        return lowestScore;
    }

    public static int calculateHighestNumber(int[] scores) {
        int highestScore = scores[0];
        for (int i = 0; i < scores.length; i++)
            if (scores[i] > highestScore) {
                highestScore = scores[i];
            }
        return highestScore;
    }

    public static int calculateTotal(int[] scores) {
        int totalScores = scores[0];
        for (int i = 0; i < scores.length; i++) {
            totalScores += scores[i];
        }
        return totalScores;
    }

    public static double calculateAverage(int[] scores) {
        return calculateTotal(scores) / (scores.length * 1.0);
    }

    public static void main(String[] args) {
        System.out.println("How many score do you want to give? ");
        Scanner input = new Scanner(System.in);
        int numberOfGrade = input.nextInt();
        int[] grades = new int[numberOfGrade];

        for (int i = 0; i < grades.length; i++) {
            System.out.println("Enter score: " + (i + 1));
            grades[i] = input.nextInt();
        }
        System.out.println("Lowest number is: " + calculateLowestNumber(grades));
        System.out.println("Highest number is: " + calculateHighestNumber(grades));
        System.out.println("Total is: " + calculateTotal(grades));
        System.out.println("Average is: " + calculateAverage(grades));

        for (int grade : grades) {
            System.out.println(grade + "");
        }
    }
}