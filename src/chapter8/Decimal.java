package chapter8;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.text.NumberFormat;

public class Decimal {
    public static void main(String[] args) {
        BigDecimal account= BigDecimal.valueOf(3844353543907.3480238944);
        NumberFormat formatter = NumberFormat.getInstance();
        formatter.setGroupingUsed(true);
        formatter.setMaximumFractionDigits(2); //rounding mood
       // System.out.println(account);
    //    formatter.setRoundingMode(RoundingMode.FLOOR);
       formatter.setRoundingMode(RoundingMode.CEILING);
        System.out.println(formatter.format(account));
    }
}
