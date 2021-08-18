package exercise;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class AutomaticBikeTest {

    @Test
    void testIfBikeCanBeTurnOn(){
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.turnOn(true);
        assertTrue(true);
    }
    @Test
     void testIfBikeCanBeTurnOff() {
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.turnOn(false);
        assertFalse(false);
    }
    @Test
    void testThatBikeCanAccelerateAtGearOne() {
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.setSpeed(15);
        timiBike.accelerateIncrease(1);
        assertEquals(16, timiBike.getCurrentSpeed());
    }

    @Test
    void testThatBikeCanAccelerateAtGearTwo() {
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.setSpeed(24);
        timiBike.accelerateIncrease(2);
        assertEquals(26, timiBike.getCurrentSpeed());
    }
    @Test
    void testThatBikeCanAccelerateAtGearThree() {
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.setSpeed(35);
        timiBike.accelerateIncrease(3);
        assertEquals(38, timiBike.getCurrentSpeed());
    }
    @Test
    void testThatBikeCanAccelerateAtGearFour(){
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.setSpeed(44);
        timiBike.accelerateIncrease(4);
        assertEquals(48, timiBike.getCurrentSpeed());
    }
    @Test
    void testThatBikeCanDeccelerateAtGearOne() {
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.setSpeed(15);
        timiBike.accelerateDecrease(1);
        assertEquals(14, timiBike.getCurrentSpeed());
    }
    @Test
    void testThatBikeCanDeecelerateAtGearTwo() {
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.setSpeed(24);
        timiBike.accelerateDecrease(2);
        assertEquals(22, timiBike.getCurrentSpeed());
    }
    @Test
    void testThatBikeCanDeecelerateAtGearThree() {
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.setSpeed(35);
        timiBike.accelerateDecrease(3);
        assertEquals(32, timiBike.getCurrentSpeed());
    }
    @Test
    void testThatBikeCanDeecelerateAtGearFour() {
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.setSpeed(44);
        timiBike.accelerateDecrease(4);
        assertEquals(40, timiBike.getCurrentSpeed());
    }
    @Test
    void testBikeRangeAccelerateForGearOne() {
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.getGear();
        timiBike.gearAccelerate(20);
        assertEquals(1, timiBike.getGear());
    }
    @Test
    void testBikeRangeAccelerateForGearTwo() {
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.getGear();
        timiBike.gearAccelerate(30);
        assertEquals(2, timiBike.getGear());
    }
    @Test
    void testBikeRangeAccelerateForGearThree() {
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.getGear();
        timiBike.gearAccelerate(40);
    }
    @Test
    void testBikeRangeAccelerateForGearFour() {
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.getGear();
        timiBike.gearAccelerate(100);
    }
    @Test
    void testBikeRangeDeecelerateForGearOne() {
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.getGear();
        timiBike.gearDeecelerate(20);
    }
    @Test
    void testBikeRangeDeecelerateForGearTwo() {
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.getGear();
        timiBike.gearDeecelerate(30);
    }
    @Test
    void testBikeRangeDeecelerateForGearThree() {
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.getGear();
        timiBike.gearDeecelerate(40);
    }
    @Test
    void testBikeRangeDeecelerateForGearFour() {
        AutomaticBike timiBike = new AutomaticBike();
        timiBike.getGear();
        timiBike.gearDeecelerate(100);
    }
}
