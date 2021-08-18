package chapter3;

import java.time.LocalDate;

public class HeartRates {
    private String firstName;
    private String lastName;
    private Date displayDay;


    public HeartRates(String firstName,String lastName, int month, int day, int year ) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.displayDay = new Date(month, day, year);
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public Date getDisplayDay() {
        return displayDay;
    }

    public void setDisplayDay(Date displayDay) {
        this.displayDay = displayDay;
    }
    public int calculateAgeInYears(){
        return LocalDate.now().getYear() - displayDay.getYear();
    }
    public int calculateTheMaximumHeartRate(){
        return 220 - displayDay.getYear();
    }
    public String calculateTheTargetHeartRate() {
        double fifthyPercentMaxHeartRate = 50 / 100 * calculateTheMaximumHeartRate();
        double eightyPercentMaxHeartRate = 80 / 100 * calculateTheMaximumHeartRate();
        return fifthyPercentMaxHeartRate + "-" + eightyPercentMaxHeartRate;
    }

    public static void main(String[] args) {
        HeartRates heart = new HeartRates("Angola", "Bello", 03, 20, 1888);

        System.out.println(heart.calculateTheMaximumHeartRate());

    }
}
