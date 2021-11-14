package src;

import com.knut.bank.*;

public class Tester {
    public static void main(String[] args) {
        MinusAccount kim = new MinusAccount(99, 200, 1000);
        // ID, 최초잔액, 한도, 마일리지 비율 순

        kim.deposit(15000);
        kim.withdraw(1000);

        System.out.println("------------------------");
        System.out.println("ID           : " + kim.getID());
        System.out.println("현재 잔고    : " + kim.get());
        System.out.println("인출가능금액 : " + kim.availableBalance());
        System.out.println("------------------------");
    }
}
