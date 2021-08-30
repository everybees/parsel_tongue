package chapter7;

public class Exercise2 {
    public static void main(String[] args) {
        int[] array = {37, 28, 88, 54, 27, 78,};
        System.out.printf("%s%8s%n", "Index", "Value");
        for (int i = 0; i < array.length; i++) {
            System.out.printf("%5d%8d%n", i, array[i]);
        }
    }
}