package chapter7;

public class XOXOArrays {
    public static void main(String[] args) {
        char[][] xoxoArrays = {{'x', ' ', 'o', ' ', 'x'}, {'o', ' ', 'x', ' ', 'o'}, {'x', ' ', 'o', ' ', 'x'}};
        for (int i = 0; i < xoxoArrays.length; i++) {
            for(int j=0; j<xoxoArrays[i].length;j++) {
                System.out.println(xoxoArrays[i][j]);
            }
        }
    }
}
