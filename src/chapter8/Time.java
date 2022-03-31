package chapter8;

public class Time {
    private int second;
    private int minute;
    private int hour;

    public void setTime(int... time) {
        hour = time[0];
        minute = time[1];
        second = time[2];
    }

    public void setTime(int hour, int second, int minute) {
        boolean hourIsNotValid = hour < 0 || hour > 23;
        if (hourIsNotValid) throw new IllegalArgumentException("Hour is not valid");
        boolean minuteIsNotValid = minute < 0 || minute > 59;
        if (minuteIsNotValid) throw new IllegalArgumentException("Minute is not valid");
        boolean secondIsNotValid = second < 0 || second > 59;
        if (secondIsNotValid) throw new IllegalArgumentException("Second is not valid");
        this.hour = hour;
        this.minute = minute;
        this.second = second;
    }

}