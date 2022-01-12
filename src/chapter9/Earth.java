package chapter9;

public class Earth {
    public static void main(String[] args) {
        Vertebrate tife = new Vertebrate();
       // tife.reproduce();
        //tife.move();
        tife.parentMove();
        tife.setEyes(59);
        System.out.println(tife.getEyes());
    }
}
