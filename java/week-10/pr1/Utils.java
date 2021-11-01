public class Utils {
    public int findMax(Compare obj, int b, int e) {
        int max = b;

        for (int i = b; i < e; i++) {
            if (obj.isGreat(i, max)) {
                max = i;
            }
        }
        return max;
    }

    public int sort() {
    }
}
