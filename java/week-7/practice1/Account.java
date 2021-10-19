public class Account {
    double balance;

    public Account() {
        this(0);
    }

    public Account(int amount) {
        balance = amount;
    }

    public double get() {
        return balance;
    }

    public void deposit(int amount) {
        balance += amount;
    }

    public void withdraw(int amount) {
        balance -= amount;
    }
}
