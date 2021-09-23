package exercise;

import org.junit.jupiter.api.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.jupiter.api.Assertions.*;

public class OkadaTest {
    @Test
    void okadaCanBeTurnOnTest() {
        Okada okada = new Okada();
        assertFalse(okada.isOn());

        okada.turnOn();
        assertTrue(okada.isOn());
    }
    @Test
    public void okadaCanBeTurnOnOff() {
        Okada okada = new Okada();
        okada.turnOn();
        assertTrue(okada.isOn());
        okada.turnOff();
        assertFalse(okada.isOn());
    }
    @Test
    void okadaCanBeAcceleratedOnGearOneTest() {
        Okada okada = new Okada();
        okada.turnOn();
        assertEquals(0, okada.getCurrentSpeed());
        assertEquals(1, okada.getCurrentGear());
        okada.accelerate();
        assertEquals(1, okada.getCurrentSpeed());
    }
    //todo test that bike cannot be accelerated when off
}
