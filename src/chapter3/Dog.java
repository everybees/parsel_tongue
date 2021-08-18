package chapter3;

public class Dog {
    private String name;
    private int age;
    private String colour;
    private String sex;
    private String type;
    CatConstructor cat = new CatConstructor("lime", "shole", "male");
    private String catName = cat.getName();

    public void move() {
        System.out.print(name + " and "+catName+" love moving around");
    }
    public void bark() {
       // move();
        System.out.print(" and he barks a lot,");
    }
    public void sleep(String sentence) {
        System.out.print(" see him sleeping like a log of wood,");
       // System.out.println(sentence);
    }
    public void bite() {
        move();
        bark();
        //sleep();
       // System.out.println(" when he was " + age + " month old" + " he bites a lot.");
    }
    public void setName(String bub) {
        name = bub;
    }
    public String getName() {
        return name;
    }
    public void setAge(int howOld) {
        age = howOld;
    }
    public int getAge() {
        return age;
    }
    public void setColour(String pink) {
        colour = pink;
    }
    public String getColour() {
        return colour;
    }
    public void setSex(String jus) {
        sex = jus;
    }
    public String getSex() {
        return sex;
    }
    public void setType(String kind) {
        type = kind;
    }
    public String getType() {
        return type;
    }
}
