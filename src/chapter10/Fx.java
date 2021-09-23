package chapter10;

public class Fx {
    public static void main(String[] args) {
        CreditCard cc = new MasterCard();
        System.out.println(cc.validate(30));
        Fish eja = new Fish();
        VisaCard card = new VisaCard();
        eja.useLessMethod(cc);

        Animal animal = new Fish();
        ((Fish) animal).useLessMethod(cc);
    }
 //   CreditCard.anotherUseLessMethod();
}
