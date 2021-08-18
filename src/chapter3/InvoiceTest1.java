package chapter3;

public class InvoiceTest1 {
    public static void main(String[] args) {
        Invoice voice = new Invoice("HDDS", "SDDSS", -1, -10);
        double net = voice.getInvoiceAmount();
        System.out.println(voice.getInvoiceAmount());
        voice.setPartNumber("XLL");
        System.out.println(voice.getPartNumber());

    }
}
