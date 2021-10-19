public class Tester1 {
    public static void main(String[] args) {
        MileageAccount kim = new MileageAccount(99, 200, 1000, 0.05);
        // ID, 최초잔액, 한도, 마일리지 비율 순

        kim.deposit(15000);
        kim.withdraw(1000);

        System.out.println("------------------------");
        System.out.println("ID           : " + kim.getID());
        System.out.println("마일리지     : " + kim.printMileage() + "%");
        System.out.println("현재 잔고    : " + kim.get());
        System.out.println("인출가능금액 : " + kim.availableBalance());
        System.out.println("------------------------");
    }
}
