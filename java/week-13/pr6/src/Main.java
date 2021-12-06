import java.util.Vector;

import javax.swing.JProgressBar;

public class Main {
    public static void main(String[] args) {
        Storage<String> data = new Storage<String>();
        Storage<BarThread> t = new Storage<BarThread>();
        Vector<String> v = new Vector<String>();
        Storage<Integer> data1 = new Storage<Integer>();
        Vector<Integer> data2 = new Vector<Integer>();

        data.set("Good");
        t.set(new BarThread(new JProgressBar()));

        System.out.println(data.get());

    }
}
