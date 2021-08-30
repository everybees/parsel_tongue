package chapter8;

public class TimeValidate {
    private int second;
    private int minute;
    private int hour;

    public void setTime(int hour, int second, int minute) {
        validate(hour, second, minute);
        this.hour = hour;
        this.minute = minute;
        this.second = second;
    }
    private void validate(int hour, int second, int minute){
        validateHour(hour);
        //validateMinute(minute);
        validateSecond(second);
    }
    public void setHour(int hour){
        validateHour(hour);
        this.hour = hour;
    }
    public void setSecond(int second){
        validateSecond(second);
        this.second = second;
    }

    private void validateSecond(int second) {

    }

    private void validateHour(int hour){boolean hourIsNotValid = hour < 0 || hour > 23;
    if (hourIsNotValid) throw new IllegalArgumentException("");
    }



    @Override
    public String toString(){
        String timeToReturn ="";
                timeToReturn += "Hour:" + hour + "\nMinute:" + minute +  "\nSecond:" + second;
                return timeToReturn;
    }
}

