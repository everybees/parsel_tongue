package MYERSBRIGGS;

import java.util.Scanner;

public class MyersBriggs {
    public static String[] questionnaire;
    public static char[] nativeInput;

    public static String[] questionnaireInArray() {
        String[] questionnaire = {
                """
                MB Question 1
                a. expend energy, enjoy groups
                b. conserve energy, enjoy one-on-one
                """,
                """
                MB Question 2
                a. interpret literally
                b. look for meaning and possibilities
                """,
                """
                MB Question 3
                a. logical, thinking, questioning
                b. empathetic, feeling, accommodating
                """,
                """
                MB Question 4
                a. organized, orderly
                b. flexible, adaptable
                """,
                """
                MB Question 5
                a. more outgoing, think out loud
                b. more reserved, think to yourself
                """,
                """
                MB Question 6
                a. practical, realistic, experiential
                b. imaginative, innovative, theortical
                """,
                """
                MB Question 7
                a. candid, straight forward, frank
                b. tactful, kind, encouraging
                """,
                """
                MB Question 8
                a. plan, schedule
                b. unplanned, spontaneous
                """,
                """
                MB Question 9
                a. seek many tasks, public activities, interaction with others
                b. seek private, solitary activities with quiet to concentrate
                """,
                """
                MB Question 10
                a. standard, usual, conventional
                b. different, novel, unique
                """,
                """
                MB Question 11
                a. firm, tend to criticize, hold the line 
                b. gentle, tend to appreciate, conciliate
                """,
                """
                MB Question 12
                a. regulated, structured
                b. easygoing, "live" and "let live"
                """,
                """
                MB Question 13
                a. external, communicative, express yourself
                b. internal, reticent, keep to yourself
                """,
                """
                MB Question 14
                a. focus on here-and-now
                b. look to the future, global perspective, 'big picture'
                """,
                """
                MB Question 15
                a. tough-minded, just
                b. tender-hearted, merciful
                """,
                """
                MB Question 16
                a. preparation, plan ahead
                b. go with the flow, adapt as you go
                """,
                """
                MB Question 17
                a. active, initiate
                b. reflective, deliberate
                """,
                """
                MB Question 18
                a. facts, things, 'what is'
                b. ideas, dreams, "what could be", philosophical
                """,
                """
                MB Question 19
                a. matter of fact, issue-oriented
                b. sensitive, people-oriented, compassionate
                """,
                """
                MB Question 20
                a. control, govern
                b. latitude, freedom
                """,
        };
        return questionnaire;
    }
    public static void collectNativeInput() {
        questionnaire = questionnaireInArray();
        Scanner input = new Scanner(System.in);
        nativeInput = new char[questionnaire.length];
        System.out.println("The Myers Briggs Questionnaire");
        System.out.println("Choose your personality description");
        for (int i = 0; i < questionnaire.length; i++) {
            System.out.println(questionnaire[i]);
            nativeInput[i] = input.next().charAt(0);
        }
    }
    public static void displayTotalUserResult() {
        String header = String.format("%5s%5s%5s", " ", "A", "B");
        System.out.println(header.repeat(4));
        System.out.println();
        System.out.println("-".repeat(62));
        for (int i = 1; i < questionnaire.length; i+=4) {
            System.out.printf("%5d", i);
            if (nativeInput[i-1] == 'a' || nativeInput[i-1] == 'A') {
                System.out.printf("%5s%5s", "a", " ");
            } else {
                System.out.printf("%5s%5s", " ", "b");
            }
            System.out.printf("%5d", i+1);
            if (nativeInput[i] == 'a' || nativeInput[i] == 'A') {
                System.out.printf("%5s%5s", "a", " ");
            } else {
                System.out.printf("%5s%5s", " ", "b");
            }
            System.out.printf("%5d", i+2);
            if (nativeInput[i+1] == 'a' || nativeInput[i+1] == 'A') {
                System.out.printf("%5s%5s", "a", " ");
            }else {
                System.out.printf("%5s%5s", " ", "b");
            }
            System.out.printf("%5d", i+3);
            if (nativeInput[i+2] == 'a' || nativeInput[i+2] == 'A') {
                System.out.printf("%5s%5s", "a", " ");
            } else {
                System.out.printf("%5s%5s", " ", "b");
            }
            System.out.println();
            System.out.print("=".repeat(62));
            System.out.println();
        }
    }
    public static void displayTotalTestResult() {
        String[] character = new String[4];
        System.out.print("Total");

        int count_a = 0;
        int count_b = 0;
        for (int i = 0; i < 4; i++) {
            if (nativeInput[i] == 'a' || nativeInput[i] == 'A') {
                count_a++;
            }else {
                count_b++;
            }

            }
        }
    }


