public class Sort {
    private int temp;

    public void sort(int n, int m) {
        if (n > m) {
            temp = m;
            m = n;
            n = temp;
        }
    }
}
