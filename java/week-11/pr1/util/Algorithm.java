package util;

public class Algorithm {
    public int findMax(Compare obj, int b, int e) {
        int max = b;
        for (int i = b; i <= e; i++) {
            if (obj.isGreater(i, max)) {
                max = i;
            }
        }
        return max;
    }
}
