package chapter4;

import java.util.Scanner;

public class FinancialApplication {

    public static void main(String[] args) {
       int tuition = 10000;
       int interest;
        for(int tuitionOfTenYear =1; tuitionOfTenYear<=10; tuitionOfTenYear++) {
         System.out.println("TuitionFeeYearly"+  ":");
            interest = (tuition * 5) /100;
         tuition = tuition +interest ;
//            tuitionOfTenYear ++;
            System.out.println(tuition+ "");
        }

    }
}
