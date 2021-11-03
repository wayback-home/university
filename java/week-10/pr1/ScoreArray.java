import java.util.Random;

public class ScoreArray implements Compare {
    private int[] data;

    public void Random() {
        Random r = new Random();
        data = new int[10];
        for (int i = 0; i < 10; i++) {
            data[i] = r.nextInt(100);
        }
    }

    public int getItem(int idx) {
        return data[idx];
    }

    public static void main(String[] args) {
        ScoreArray array = new ScoreArray();
        Sort algorythm = new Sort();

    }

    @Override
    public void swap() {
        ;
    }
}
