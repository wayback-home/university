package bank;

public class Account {
    public int balance;

    public Account() {
        balance = 0;
    }

    public void set(int amount) {
        balance = amount;
    }

    public int get() {
        return balance;
    }
}
