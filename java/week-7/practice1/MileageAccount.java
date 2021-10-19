public class MileageAccount extends MinusAccount {
    private double mileage;

    public MileageAccount(int id, int balance, int limit, double getMileage) {
        super(id, balance, limit);
        mileage = getMileage;
    }

    public double printMileage() {
        return (int) (mileage * 100);
    }

    public void deposit(int amount) {
        balance = balance + amount * (1 + mileage);
    }
}
