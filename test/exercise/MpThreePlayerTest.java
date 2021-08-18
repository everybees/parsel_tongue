package exercise;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class MpThreePlayerTest {
    @Test
    void mpThreePlayerCanBeOnTest() {
        MpThreePlayer palito = new MpThreePlayer();
        assertFalse(palito.isOn());

        palito.turnOn();
        assertTrue(palito.isOn());
    }

    @Test
    void mpThreePlayerCanBeOffTest() {
        MpThreePlayer palito = new MpThreePlayer();
        palito.turnOn();
        assertTrue(palito.isOn());

        palito.turnOff();
        assertFalse(palito.isOn());
    }
    @Test
    void mpThreePlayerVolumeCanBeIncreaseTest() {
        MpThreePlayer palito = new MpThreePlayer();
        palito.increaseVolume();
        palito.increaseVolume();
        palito.increaseVolume();
        palito.increaseVolume();
        assertEquals(4, palito.getVolume());
    }
    @Test
    void mpThreeplayerVolumeCaBeDecereaseTest() {
        MpThreePlayer palito = new MpThreePlayer();
        palito.decreaseVolume();
        assertEquals(0, palito.getVolume());
    }
    @Test
    void  mpThreePLayerCanPlayTest() {
        MpThreePlayer palito = new MpThreePlayer();
        palito.play(true);
        assertTrue(palito.getPlayer());
    }
    @Test
    void mpThreePlayerCanPauseTest() {
        MpThreePlayer palito = new MpThreePlayer();
        palito.pause(false);
        assertFalse(palito.getPlayer());
    }
    @Test void mpThreePLayerCanChangeSongTest() {
        MpThreePlayer palito = new MpThreePlayer();
        palito.songChanged();
        palito.songChanged();
        palito.songChanged();
        assertEquals(3, palito.getChanged());
    }
}