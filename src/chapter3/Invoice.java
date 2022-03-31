package chapter3;

public class Invoice {
    private String partNumber;
    private String partDescription;
    private int quantityOfTheItem;
    private double pricePerItem;

    public Invoice(String partNumber, String partDescription, int quantityOfTheItem, double pricePerItem) {
        this.partNumber = partNumber;
        this.partDescription = partDescription;
        this.quantityOfTheItem = quantityOfTheItem;
        this.pricePerItem = pricePerItem;
    }
    public void setPartNumber(String partNumber) {
        this.partNumber = partNumber;
    }
    public void setPartDescription(String partDescription) {
        this.partDescription = partDescription;
    }
    public void setQuantityOfTheItem(int quantityOfTheItem) {
        this.quantityOfTheItem = quantityOfTheItem;
    }
    public void setPricePerItem(double pricePerItem) {
        this.pricePerItem = pricePerItem;
    }
    public String getPartNumber() {
        return partNumber;
    }
    public String getPartDescription() {
        return partDescription;
    }
    public int getQuantityOfTheItem() {
        return quantityOfTheItem;
    }
    public double getPricePerItem() {
        return pricePerItem;
    }
    public double getInvoiceAmount() {
    if (quantityOfTheItem < 0 || pricePerItem < 0){
        return 0.0;
    }
        return pricePerItem * quantityOfTheItem;
    }
}
