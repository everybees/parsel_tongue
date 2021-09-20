package credit_calculator;

public class Item {
    private String name;
    private double price;


    public Item(String name, double price){
        this.name = name;
        this.price = price;
    }

    @Override
    public String toString() {
        return
                "name='" + name + '\'' +
                ", price=" + price +
                '}';
    }
}
