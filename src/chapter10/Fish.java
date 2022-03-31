package chapter10;

public class Fish extends Animal{
    @Override
    public void move(){
        System.out.println("swim well");
    }
    public void useLessMethod(CreditCard cc){
        cc.validate( 30);
    }
}
