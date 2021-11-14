package src;

import java.util.Random;

public class Customer {
    private int id, balance;

    public Customer(int n) {
        id = n;
        Random r = new Random();
        balance = r.nextInt(90000000) + 10000000;
    }

    public int getID() {
        return id;
    }

    public int getBalance() {
        return balance;
    }

    public String get() {
        return "ID : " + id + "\nBalance : " + balance;
    }
}
