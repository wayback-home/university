public class Tester1 {
    public static void main(String[] args) {
        MinusAccount kim = new MinusAccount(99, 200, 1000);

        kim.deposit(150);
        kim.withdraw(1000);

        System.out.println("---------------------");
        System.out.println("ID           : " + kim.getID());
        System.out.println("현재 잔고    : " + kim.get());
        System.out.println("인출가능금액 : " + kim.availableBalance());
        System.out.println("---------------------");
    }
}
