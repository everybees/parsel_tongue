package exercise;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TelevisionTest {
    @Test
    void testThatTelevisionCanOn() {
        Television sony = new Television();
        sony.isOn(true);
        assertTrue(sony.getPower());
    }
    @Test
    void testThatTelevisionCanOff() {
        Television sony = new Television();
        sony.isOn(false);
        assertFalse(sony.getPower());
    }
    @Test
    void testThatTelevisionCanChangeChannel() {
        Television sony = new Television();
        sony.setChannel(1);
        assertEquals(1, sony.getChannel());
    }
    @Test
    void testThatTelevisionVolumeCanBeIncreased() {
     Television sony =  new Television();
     sony.increaseVolume();
     assertEquals(1, sony.getVolume());
    }
    @Test
    void testThatTelevisionVolumeCanBeDecrease() {
        Television sony = new Television();
        sony.decreaseVolume();
        assertEquals(-1, sony.getVolume());

    }
}