package chapter5;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class PriceCopyTest {
    @Test
    void calculatePriceOf1To4CopiesTest(){
        PriceCopy perCopy = new PriceCopy();
        int price = perCopy.calculatePrice(2);
        assertEquals(3000, price);
        price = perCopy.calculatePrice(1);
        assertEquals(1500, price);
        price = perCopy.calculatePrice(3);
        assertEquals(4500, price);
        price = perCopy.calculatePrice(4);
        assertEquals(6000, price);
    }
    @Test
    void calculatePriceOf5To9CopiesTest() {
        PriceCopy perCopy = new PriceCopy();
        assertEquals(9800, perCopy.calculatePrice(7));
        assertEquals(8400, perCopy.calculatePrice(6));
    }
    @Test
    void calculatePriceTheOf10To29CopiesTest(){
        PriceCopy perCopy = new PriceCopy();
        assertEquals(14400, perCopy.calculatePrice(12));
        assertEquals(30000, perCopy.calculatePrice(25));
    }

    @Test
    void calculatePriceTheOf30To39CopiesTest(){
        PriceCopy perCopy = new PriceCopy();
        assertEquals(35200, perCopy.calculatePrice(32));
        assertEquals(41800, perCopy.calculatePrice(38));
    }
    @Test
    void calculatePriceTheOf50To99CopiesTest(){
        PriceCopy perCopy = new PriceCopy();
        assertEquals(60000, perCopy.calculatePrice(60));
        assertEquals(70000, perCopy.calculatePrice(70));
    }
    @Test
    void calculatePriceTheOf100To199CopiesTest(){
        PriceCopy perCopy = new PriceCopy();
        assertEquals(108000, perCopy.calculatePrice(120));
        assertEquals(162000, perCopy.calculatePrice(180));
    }
    @Test
    void calculatePriceTheOf200AboveCopiesTest(){
        PriceCopy perCopy = new PriceCopy();
        assertEquals(200000, perCopy.calculatePrice(250));
        assertEquals(2400000, perCopy.calculatePrice(3000));
    }
}
