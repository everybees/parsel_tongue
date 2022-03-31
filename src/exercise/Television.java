package exercise;

public class Television {
    private int channel;
    private boolean isOn;
    private int volume;

    public void isOn(boolean isOn) {
        this.isOn = isOn;
    }

    public boolean getPower() {
        return isOn;
    }

    public void setChannel(int channel) {
        this.channel = channel;
    }

    public int getChannel() {
        return channel;
    }

    public void increaseVolume() {
        this.volume = volume + 1;
    }

    public int getVolume() {
        return volume;
    }

    public void decreaseVolume() {
        this.volume = volume - 1;
    }
}
