package exercise;

public class Okada {
    private boolean isOn;
    private int currentSpeed;
    private int currentGear = 1;

    public boolean isOn() {
        return isOn;
    }
    public void turnOn() {
        this.isOn = true;
    }

    public void turnOff() {
        this.isOn = false;
    }

    public int getCurrentSpeed() {
        return currentSpeed;
    }

    public void accelerate() {
        if (currentSpeed >= 21) {
            currentSpeed += 1;
            currentSpeed += 2;
        }
        if (currentSpeed <= 20) {
            currentSpeed = currentSpeed + 1;
            if (currentSpeed == 21) {
                currentGear = 2;
            }
        }
    }
    public int getCurrentGear() {
        return currentGear;
    }
}
