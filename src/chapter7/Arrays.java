package chapter7;

public class Arrays {
    public static void main(String[] args) {
        int[] scores = {35,27,98,134,66543,894,};
////        for(int score: scores) {
////            System.out.println(score);
//        }
        for (int i = 0; i < 6; i++) {
            scores[i] = i * i;
        }
            for (int score: scores) {
                System.out.println(score + " ");
            }

//        for(int i = 0; i <= 6; i++){
//            System.out.println(scores[i]);
//        }
//        System.out.println(scores[0]);
//        System.out.println(scores[1]);
    }
}
