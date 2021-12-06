import javax.swing.JFrame;
import javax.swing.JProgressBar;
import java.awt.*;

public class ShowMe extends JFrame {
    JProgressBar[] bars;
    BarThread[] threads;

    public ShowMe() {
        bars = new JProgressBar[4];
        setLayout(new GridLayout(4, 1));
        for (int i = 0; i < bars.length; i++) {
            bars[i] = new JProgressBar();
            add(bars[i]);
        }
        setSize(200, 100);
        setTitle("Draw Two Circle");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    public void begin() {
        threads = new BarThread[4];
        for (int i = 0; i < threads.length; i++) {
            threads[i] = new BarThread(bars[i]);
            threads[i].start();
        }

    }

    public static void main(String[] args) {
        ShowMe app = new ShowMe();
        app.begin();
    }
}