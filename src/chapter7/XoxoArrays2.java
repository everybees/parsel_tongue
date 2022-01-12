package chapter7;

public class XoxoArrays2 {
    public static void main(String[] args) {
        String[][] xoxoArrays1 = {{"X O X"}, {"O X O C"}, {"X O X V"}};
        for (int rowNumber = 0; rowNumber < xoxoArrays1.length; rowNumber++) {
            for (int columnNumber = 0; columnNumber < xoxoArrays1[rowNumber].length; columnNumber++) {
                System.out.println((xoxoArrays1[rowNumber][columnNumber]) + " ");
            }
            System.out.println();
        }
//    }
//    for(String[] rowArray : tictactoe) {
//        for(String columuString: rowArray){
//            System.out.println(columnStrings + " ");
//        }
//    }
        //pre and post conditions
//        for (int i = 0; i < 10; i++) {
//            System.out.println(i++ +" ");
//            System.out.println(++i + " ");
//        }

        }
}