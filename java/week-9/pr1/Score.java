public class Score {
    private int point;

    public Score(int n) {
        point = n;
    }

    public void set(int n) {
        if (n <= 100 && n >= 0) {
            point = n;
        } else {
            throw new IllegalArgumentException("input 0 to 100");
        }
    }

    public int get() {
        return point;
    }
}
