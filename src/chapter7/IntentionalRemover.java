package chapter7;

public class IntentionalRemover {
    public static void main(String[] args) {
        int counter = 1;
        counter = ++ counter + ++counter;
        System.out.println(counter);

        int counter1 = 1;
        counter1 = counter1++ + ++counter1;
        System.out.println(counter1);

        int counter2 = 1;
        counter2 = counter2 +++ counter2++;
        System.out.println(counter2);

        int counter3 = 1;
        counter3 = ++counter3 + counter3++;
        System.out.println(counter3);
    }

}
