package worksheet;

public class Main {
    public static void main(String[] args) {
        double kilometer = 100 * 1.60923;
        int highScore = 60;

        if (highScore == 60) {
            System.out.println("This is an expression");
        }

        int score = 100;
        if (score > 90) {
            System.out.println("You got it right");
            score = 0;
        }

        int myVariable = 50;
        myVariable++;
        myVariable--;
        System.out.println("This is a text");

        System.out.println("This is" +
                " another" +
                " still more. ");

        boolean scores = true;
        int grade = 2000;
        int bonus = 100;
        int levelCompleted = 5;
//        if (grade < 2000 && grade > 800) {
//            System.out.println("Your grade is less 700, great scores");
//        } else if (grade < 400) {
//            System.out.println("your grade is less than 700");
//        } else {
//            System.out.println("try again next time");
//        }

        if (scores  ) {
            int finalScore = grade + (levelCompleted * bonus);
            System.out.println("your first score is: " + finalScore);
        }
        boolean scolar = true;
        int score2 = 10000;
        int levelCompleted2 = 8;
        int bonus2 = 200;
        if (scolar) {
            int final2 = score2 + (levelCompleted2 * bonus2);
            System.out.println(" your score is: " + final2);
        }

    }
}
