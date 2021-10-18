import java.util.Random;

public class IntArray {
    int[] data;

    public IntArray() {
        data = null;
    }

    public IntArray(int n) {
        int i;
        Random r = new Random();
        data = new int[n];
        for (i = 0; i < n; i++)
            data[i] = r.nextInt(100);
    }

    public int getLength() {
        return data.length;
    }

    public int get(int idx) {
        return data[idx];
    }

    public void set(int idx, int value) {
        data[idx] = value;
    }

    public int getTotal() {
        return getTotal(0, data.length - 1);
    }

    public int getTotal(int b, int e) {
        int total = 0;
        int i;
        for (i = b; i <= e; i++)
            total += data[i];
        return total;
    }
}