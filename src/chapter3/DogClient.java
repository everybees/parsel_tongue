package chapter3;

import chapter3.Dog;

public class DogClient {
    public static void main(String[] args) {
        Dog newPet = new Dog();
        newPet.setName("Bub");
        System.out.print("The name of my dog is " +  newPet.getName());
        newPet.setAge(2);
        newPet.setColour("brown");
        System.out.print(", his colour is " + newPet.getColour());
        newPet.setSex("male");
        System.out.print(", The dog is a " + newPet.getSex());
        newPet.setType("Pit Bull");
        System.out.println(", He's a " + newPet.getType() + "."   );
       // newBigg.move();
       // newPet.bark();
        //newPet.sleep();
        newPet.bite();
//        newBigg.setAge(5);
//        System.out.println(newBigg.getAge());
        Dog newPet2 = new Dog();
        newPet2.setName("Lenny");
        System.out.print(newPet2.getName() + " is ");
        newPet2.setAge(5);
        System.out.print(newPet2.getAge() + " old,");
        newPet2.setColour("Black Brown");
        System.out.print(" her colour makes are unique " + newPet2.getColour());
        newPet2.setSex("Female");
        System.out.print(", The dog is a " + newPet2.getSex());
        newPet2.setType("German Shepherd");
        System.out.println(", she is a " + newPet2.getType() + ".");
       // newPet2.move();
//        System.out.println("lenny is a mover");
     //   newPet2.bark();
       // newPet2.sleep(newPet2.getName() +" Loves sleeping");
        newPet2.bite();

        Dog newPet3 = new Dog();
        newPet3.setColour("white");
        System.out.println(newPet3.getColour());

        Dog newPet4 = new Dog();
        newPet4.setSex("male");
        System.out.println("The dog  sex is : " + newPet4.getSex());

        Dog newPet5 = new Dog();
        newPet5.setType("Pit Bull");
        System.out.println(newPet5.getType());
    }
}
