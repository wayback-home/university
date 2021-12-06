import java.util.Random;

import javax.swing.JProgressBar;

public class BarThread extends Thread {
    JProgressBar bar;
    Random random;

    public BarThread(JProgressBar b) {
        bar = b;
        random = new Random();
    }

    public void run() {
        while (true) {
            bar.setValue(random.nextInt(101));
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

}
