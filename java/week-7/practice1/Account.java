public class Account {
    int balance;

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
        balance += amount;
    }

    public void withdraw(int amount) {
        balance -= amount;
    }
}
