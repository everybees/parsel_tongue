package credit_calculator;

public class Customer {
    private int accountNumber;
    private double balance;
    private Item item;
    private double totalCredit;

    public int getAccountNumber() {
        return accountNumber;
    }

    public void setAccountNumber(int accountNumber) {
        this.accountNumber = accountNumber;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }

    public Item getItem() {
        return item;
    }

    public void setItem(Item item) {
        this.item = item;
    }

    public double getTotalCredit() {
        return totalCredit;
    }

    public void setTotalCredit(double totalCredit) {
        this.totalCredit = totalCredit;
    }
    public Item buyItem(Item item){
        return item;
    }

    @Override
    public String toString() {
        return
                "balance=" + balance +
                ", item=" + item +
                ", totalCredit=" + totalCredit +
                '}';
    }
}
