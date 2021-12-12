import java.util.Random;

public class ScoreArray implements Compare {
    private int[] data;

    public int Random() {
        int temp;
        Random r = new Random();
        temp = r.nextInt(100);
        return temp;

    }

    public void setting() {
        data = new int[10];
        for (int i = 0; i < data.length; i++) {
            data[i] = Random();
        }
    }

    public void returnData() {
        for (int i = 0; i < data.length; i++) {
            System.out.println(data[i]);
        }
    }
    // public int getItem(int idx) {
    // return data[idx];
    // }

    public static void main(String[] args) {
        ScoreArray array = new ScoreArray();
        array.setting();
        array.returnData();

        Utils algorythm = new Utils();
        algorythm.findMax(array, 0, 10);

    }

    @Override
    public boolean isGreat(int n, int m) {
        return data[n] > data[m];
    }

    @Override
    public void swap(int n, int m) {
        int temp;
        for (int i = 0; i < 10; i++) {

            if (isGreat(i, i + 1) == true) {
                temp = data[i + 1];
                data[i + 1] = data[i];
                data[i] = temp;
            }
        }
    }
}