package chapter3;

public class CatConstructor {
    private String name;
    private String colour;
    private String sex;
    Dog newPet = new Dog();
    private String name2 ;

    public CatConstructor(String name, String colour, String sex){
        this.name = name;
        this.colour = colour;
        this.sex = sex;
        name2 = newPet.getName();
    }
    public String getName(){
        return name;
       // return name + colour + sex;
    }
    public String getColour() {
        return colour;
    }
    public String getSex() {
        return sex;
    }

    public static void main(String[] args) {
        CatConstructor cat = new CatConstructor("lenny", "black", "female");
        System.out.println(cat.getSex());
        String name = cat.getName();
        System.out.println(name);

        CatConstructor cat2 = new CatConstructor("sholly", "brown", "male");
        System.out.println(cat2.getColour() + " " + cat2.getName());
       // System.out.println(cat2.getName());
    }
}
