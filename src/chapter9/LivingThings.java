package chapter9;

public class LivingThings {
    private  int eyes;

    public  LivingThings(){
        System.out.println("Who can create LivingThings?");
    }
    public  void reproduce() {
        System.out.println("Be fruitful and multiply and replenish");
    }
    public void move() {
        System.out.println("Walk walk");
    }
    public  void die() {
        System.out.println("dont die");
    }

    public int getEyes() {
        return eyes;
    }

    public void setEyes(int eyes) {
        this.eyes = eyes;
    }
}
