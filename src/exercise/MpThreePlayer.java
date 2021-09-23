package exercise;

public class MpThreePlayer {
    private boolean isOn;
    private int volume;
    private boolean player;
    private int songChanged;

    public boolean isOn() {
        return isOn;
    }

    public void turnOn() {
        this.isOn = true;
    }

    public void turnOff() {
        this.isOn = false;
    }

    public void increaseVolume() {
        volume += 1;
    }

    public int getVolume() {
        return volume;
    }

    public void decreaseVolume() {
        if (volume >= 30)
            volume -= 1;
    }

    public void play(boolean play) {
        this.player = play;
    }

    public boolean getPlayer() {
        return player;
    }

    public void pause(boolean pause) {
        this.player = pause;
    }

    public void songChanged() {
        songChanged = songChanged + 1;
    }

    public int getChanged() {
        return songChanged;
    }
}
