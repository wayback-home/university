public class Tester1 {
    public static void main(String[] args) {
        CustomerAccount kim = new CustomerAccount(99);

        kim.deposit(1000);

        System.out.println(kim.get());
        System.out.println(kim.getID());
    }
}
