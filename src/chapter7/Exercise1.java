package chapter7;

public class Exercise1 {
    public static void main(String[] args) {
        int[] array = new int[10];
        for (int i = 0; i < 10; i++) {
            array[i] = i*2;

        }
        System.out.printf("%s%8s%n", "Index", "Value");
        for (int i = 0; i < array.length; i++) {
      //      array[i] = 2 + 2 * i;
            System.out.printf("%5d%8d%n", i, array[i]);
        }
    }
}
