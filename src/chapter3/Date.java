package chapter3;

public class Date {
    private int month;
    private int day;
    private int year;

    public Date(int month, int day, int year) {
        this.month = month;
        this.day = day;
        this.year = year;
    }
    public void setMonth(int month){
        this.month = month;
    }
    public void setDay(int day){
        this.day = day;
    }
    public void setYear(int year) {
        this.year = year;
    }
    public int getMonth(){
        return month;
    }
    public int getDay() {
        return day;
    }
    public int getYear() {
        return year;
    }
    public String displayDate(){
        return month + "/" + day + "/" + year;
    }
    public static void main(String[] args) {
    Date displayDate = new Date(5, 26, 1995);
    displayDate.displayDate();
       System.out.println(displayDate.displayDate());
    }
}
