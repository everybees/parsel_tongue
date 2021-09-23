package chapter7;

public class HighestLowestReduced {
    public static int calculateTotal(int[] results){
        int total = results[0];
        for (int i = 0; i < results.length; i++) {
            total += results[i];
        }
        return total;
    }
    public static int calculateHighestScore(int[] results){
        int highScore = results[0];
        for (int i = 0; i < results.length; i++)
            if (results[i] > highScore){
                highScore = results[i];
            }
            return highScore;
        }
    public static int calculateLowestScore(int[] results){
        int lowestScore = results[0];
        for (int i = 0; i < results.length; i++)
            if (results[i] < lowestScore) {
                lowestScore = results[i];
            }
            return  lowestScore;
    }
    public  static int calculateTheFirstNumber(int[] results) {
        int firstNumber = results[0];
        for (int i = 0; i < results.length; i++){
        } return calculateHighestScore(results) - calculateTotal(results);
    }
    public static int calculateTheSecondNumber(int[] results) {
        int secondNumber = results[0];
        for (int i = 0; i < results.length; i++) {
        }return calculateLowestScore(results) - calculateTotal(results);
    }
    public static void main(String[] args) {
        System.out.println("The highest score is: " + calculateHighestScore(new int[]{3,5,8,500, 1295, 1324245, 9}));
        System.out.println("The lowest score is: " + calculateLowestScore(new int[] {7,20,573,}));
    }
}
