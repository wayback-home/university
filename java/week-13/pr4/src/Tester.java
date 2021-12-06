public class Tester {
    public static void main(String[] args) {
        Counter c = new Counter();
        c.start();

        try {
            Thread.sleep(2500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        c.interrupt();
        try {
            c.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
