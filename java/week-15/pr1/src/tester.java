import java.util.Iterator;
import java.util.Vector;

public class tester {
    public static void main(String[] args) {
        Vector<String> data = new Vector<String>();
        // Vector<String> data = new Vector<>();
        // var data = new Vector<String>();

        data.add("Good");
        data.add(0, "Morning");
        data.add("Hello");

        for (int i = 0; i < data.size(); i++) {
            System.out.println(data.get(i));
        }

        Iterator<String> iter = data.iterator();
        while (iter.hasNext()) {
            System.out.println(iter.next());
        }
        for (String str : data) {
            System.out.println(str);
        }

    }
}
