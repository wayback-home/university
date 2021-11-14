package src;

import com.knut.utils.*;

public class CustomerAccount {

    public static void main(String[] args) {
        Customer[] customers = new Customer[10];
        for (int i = 0; i < 10; i++) {
            customers[i] = new Customer(i);
        }

        Utils algorythm = new Utils();
        Sort getset = new Sort();
        // 최고잔액 출력
        System.out.println(algorythm.findMax(customers, 0, 10));

        System.out.println(customers[3].get());

    }

}
