package chapter7;

public class BarChart {
    public static void main(String[] args) {
        int[] array = {0,1,2,2,3,3,4,4,5,6};
        System.out.println("grade distribution");
        for (int a = 0; a < array.length; a++) {
            if (a == 10 )
                System.out.printf("%5d: ", 100);
            else
                System.out.printf("%02d - %02d: ", a * 10, a * 10 + 9);
            for (int i = 0; i < array[a]; i++) {
                System.out.print("*");
                System.out.println();
            }
        }
    }
}
