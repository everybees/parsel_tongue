package chapter5;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class KataTest {
@Test
   public void calculateFactorialTest(){
        Kata kata = new Kata();
        int result = kata.calculateFactorialOf(3);
        assertEquals(6, result);
    }

    @Test
    public void calculateSquareTest() {
    Kata kata = new Kata();
    int result = kata.calculateSquareOf(5);
    assertEquals(25, result);

    }
}
