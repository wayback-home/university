package src;

public class TotalMain {
    private long total;
    private Calculator[] calcs;

    public TotalMain() {
        total = 0;
        calcs = new Calculator[10];
        for (int i = 0; i < calcs.length; i++) {
            calcs[i] = new Calculator(this, i * 1000000, i * 1000000 + 999999);
            calcs[i].start();
        }
    }

    public synchronized void add(int n) {
        total += n;
    }

    public long get() {
        for (int i = 0; i < calcs.length; i++) {
            try {
                calcs[i].join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        return total;
    }

    public static void main(String[] args) {
        TotalMain t = new TotalMain();
        System.out.println("Total = " + t.get());
    }
}
