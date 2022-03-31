package exercise;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class AirConditionerTest {
    @Test
    void acCanBeTurnedOnTest(){
        AirConditioner sharp = new AirConditioner();

        // AirConditioner thermocool = new AirConditioner();
        assertFalse(sharp.isOn());

        sharp.setOn(true);

        // sharp.SwitchOff();

        assertTrue(sharp.isOn());
    }
    @Test
    void acCanBeTurnedOffTest(){
        AirConditioner sharp = new AirConditioner();
        //sharp.setOn(true);
        sharp.setOn(false);
        assertFalse(sharp.isOn());
    }

    @Test
    void temperatureCanBeIncreasedTest(){
        AirConditioner suAc = new AirConditioner();
        suAc.setOn(true);
        suAc.increaseTemperature();
        assertEquals(30, suAc.getCurrentTemperature());
    }
    }

