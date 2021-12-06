public class Counter extends Thread {
    public void run() {
        int count = 0;

        super.run();
        while (true) {
            count += 1;
            System.out.println("count = " + count);

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
                break;
            }
        }
    }
}
