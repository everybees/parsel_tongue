package chapter10;

public class Forest {
    public static void main(String[] args) {
        Animal[] animals = new Animal[5];
        animals[0] = new Frog();
        animals[1] = new Bird();
        animals[2] = new Fish();
        animals[3] = new Animal();

        for (Animal animal: animals) {
            animal.move();
        }
        Animal animal;
        animal = new Fish();
        animal = new Bird();
        animal = new Frog();
        Frog opolo;
        opolo = (Frog) new Animal();
    }
}
