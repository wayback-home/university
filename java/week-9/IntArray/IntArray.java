public class IntArray implements Compare {

    private int[] data;

    public IntArray() {
        data = new int[5];
        data[0] = 5;
        data[1] = 10;
        data[2] = 99;
        data[3] = 0;
        data[4] = 15;
    }

    public static void main(String[] args) {
        IntArray array = new IntArray();
        Utils algorythm = new Utils();

        System.out.println(algorythm.findMax(array, 0, 4));
    }

    @Override
    public boolean isGreat(int n, int m) {
        return data[n] > data[m];
    }
}
