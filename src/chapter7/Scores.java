package chapter7;

import java.util.Scanner;

public class Scores {
    public static void main(String[] args) {
        int[] scores = {23, 10, 41, 15, 14, 18, 19, 49, 20, 50};
        int highestScore = 0;
        int lowestScore = scores[0];
        int totalScore = 0;
        double averageScore = 0;
        int i;
        for (i = 0; i < scores.length; i++) {
            totalScore += scores[i];
            averageScore = (double) totalScore / 10;

            if (scores[i] < lowestScore) {
                lowestScore = scores[i];
            }
            if (scores[i] > highestScore) {
                highestScore = scores[i];
            }
        }
        System.out.printf(" totalscore: %d%n averagescore: %f%n lowestscore: %d%n highestscore: %d%n", totalScore, averageScore, lowestScore, highestScore);
    }
}
