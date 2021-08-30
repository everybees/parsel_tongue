package chapter3;

import java.time.LocalDate;
import java.util.Scanner;

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
        return 220 - calculateAgeInYears();
    }
    public String calculateTheTargetHeartRate() {
        double fifthyPercentMaxHeartRate = (50.0 / 100) * calculateTheMaximumHeartRate();
        double eightyPercentMaxHeartRate = 80.0 / 100 * calculateTheMaximumHeartRate();
        return fifthyPercentMaxHeartRate + "-" + eightyPercentMaxHeartRate;
    }

    public static void main(String[] args) {
//        Scanner input = new Scanner(System.in);
//        System.out.println("Enter your first name: ");
//        String firstName = input.nextLine();
//        System.out.println("Enter your last name: ");
//        String lastName = input.nextLine();
//        System.out.println("Enter your month");
//        int month = input.nextInt();
//        System.out.println("Enter your day");
//        int day = input.nextInt();
//        System.out.println("Enter your year");
//        int year = input.nextInt();
//
//        HeartRates heart = new HeartRates(firstName, lastName, month, day, year);
        HeartRates heart = new HeartRates("Buki", "Jonah", 12, 31, 1993);
        System.out.println("Your age in year is: " + heart.calculateAgeInYears());
        System.out.println(heart.calculateTheMaximumHeartRate());
        System.out.println(heart.calculateTheTargetHeartRate());

    }
}
