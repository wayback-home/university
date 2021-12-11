public class Account {
    private int balance;

    public Account() {
        this(0);
    }

    public Account(int amount) {
        balance = amount;
    }

    public int get() {
        return balance;
    }

    public void deposit(int amount) {
        if (amount >= 0) {
            balance += amount;
        } else {
            throw new IllegalArgumentException();
        }
    }

    public void withdraw(int amount) {
        if (amount <= balance && amount >= 0) {
            balance -= amount;
        } else {
            throw new IllegalArgumentException();
        }
    }
}
