package exercise;

public class AutomaticBike {

    private boolean power;
    private int speed;
    private int gear;

    public void turnOn(boolean isOn) {

        this.power = isOn;
    }

    public boolean turnOn() {
        return power;
    }

    public void accelerateIncrease(int gear) {
        if (gear == 1)
            speed = speed + 1;
        if (gear == 2)
            speed = speed + 2;
        if (gear == 3)
            speed = speed + 3;
        if (gear == 4)
            speed = speed + 4;
    }

    public void setSpeed(int speed) {
        this.speed = speed;
    }

    public int getCurrentSpeed() {
        return speed;
    }

    public void accelerateDecrease(int gear) {
        if (gear == 1)
            speed = speed - 1;
        if (gear == 2)
            speed = speed - 2;
        if (gear == 3)
            speed = speed - 3;
        if (gear == 4)
            speed = speed - 4;
    }


    public void gearAccelerate(int speed) {
        this.speed = speed;
        if (speed >= 0 && speed <= 20) {
            gear = 1;
        }
        if (speed >= 21 && speed <= 30) {
            gear = 2;
        }
        if (speed >= 31 && speed <= 40) {
            gear = 3;
        }
        if (speed >= 41 && speed <= 100)
            gear = 4;
    }
    public int getGear() {
        return gear;
    }
    public void gearDeecelerate(int speed) {
        if (speed <= 0 && speed >= 20) {
            gear = 1;
        }
        if (speed <= 21 && speed >= 30) {
            gear = 2;
        }
        if (speed <= 31 && speed >= 40) {
            gear = 3;
        }
        if (speed <= 41 && speed >= 100) {
            gear = 4;
        }
    }
}

