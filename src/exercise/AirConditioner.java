package exercise;

public class AirConditioner {
    private boolean isOn;
    private Object currentTemperature;

    public boolean isOn() {
        return isOn;
    }

    public void setOn(boolean isOn) {
        this.isOn = isOn;
    }

    public void increaseTemperature() {
        //  currentTemperature = currentTemperature + 1;
    }

    public int getCurrentTemperature() {
        return 0;
    }
}
