public class Tester {
    public static void main(String[] args) {
        CounterI ci = new CounterI();

        Thread th = new Thread(ci);
        Thread th1 = new Thread(ci);
        Thread th2 = new Thread(ci);

        th.start();
        th1.start();
        th2.start();
    }
}
