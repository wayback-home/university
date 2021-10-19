public class MinusAccount extends CustomerAccount {
    private int limitMinus;

    public MinusAccount(int id, int balance, int limit) {
        super(id, balance);
        limitMinus = -limit;
    }

    public double availableBalance() {
        return -(limitMinus - balance);
    }

    public void deposit(int amount) {
        balance += amount;
    }

    public void withdraw(int amount) {
        if (balance < limitMinus) {
            System.out.println("인출할 수 없습니다");
        } else {
            if (balance - amount < limitMinus) {
                System.out.println("인출할 수 없습니다");
            } else {
                balance = balance - amount;
                System.out.println("인출 완료");
            }
        }
    }
}
