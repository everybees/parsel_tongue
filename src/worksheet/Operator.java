package worksheet;

public class Operator {
    public static void main(String[] args) {
        int result = 1 + 2;
        System.out.println("1 + 2 = " + result);
        int previousRsult = result;
        System.out.println("previousResult = " + previousRsult);
        result = result - 1;
        System.out.println("previousResult = " + previousRsult );
        result = result * 10;
        System.out.println(result);
        result = result / 5;
        System.out.println(result);
        result = result % 3;
        System.out.println(result);
    }


}
