package com.knut.bank;

public class CustomerAccount extends Account {
    int id;

    public CustomerAccount(int n) {
        super();
        id = n;
    }

    public CustomerAccount(int n, int amount) {
        super(amount);
        id = n;
    }

    public int getID() {
        return id;
    }
}
