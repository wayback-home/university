public class ScoreArray implements Compare {
    private Score[] data;

    public ScoreArray() {
        data = new Score[5];
        data[0] = new Score(5);
        data[1] = new Score(10);
        data[2] = new Score(99);
        data[3] = new Score(0);
        data[4] = new Score(15);

    }

    public Score getItem(int idx) {
        return data[idx];
    }

    public static void main(String[] args) {
        ScoreArray array = new ScoreArray();
        Utils algorythm = new Utils();

        System.out.println(algorythm.findMax(array, 0, 4));

        int idx = algorythm.findMax(array, 0, 4);
        System.out.println(array.getItem(idx).get());
    }

    @Override
    public boolean isGreat(int n, int m) {
        return data[n].get() > data[m].get();
    }
}
