public class CounterI implements Runnable {
    public void run() {
        int count = 0;

        while (true) {
            count += 1;
            System.out.println("count = " + count);

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {

                e.printStackTrace();
            }
        }
    }
}
