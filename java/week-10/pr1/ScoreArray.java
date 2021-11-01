import java.util.Random;

public class ScoreArray implements Compare {
    private Score[] data;

    public ScoreArray() {
        Random r = new Random();
        data = new Score[5];

        for (int i = 0; i < data.length; i++) {
            data[i] = r.nextInt(100);
        }
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

    @Override
    public void swap(int n, int m) {
        ;
    }
}
