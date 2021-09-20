package chapter9;

public class Vertebrate extends Animal{
    public Vertebrate(){
        //super();
        System.out.println("new Vertebrate?");
    }
    @Override
    public  void die(){
        System.out.println("Shall not ");
    }
    public void parentMove(){
        super.move();
    }
    public void move() {
        System.out.println("Go placidly");
        getEyes();
    }
}
