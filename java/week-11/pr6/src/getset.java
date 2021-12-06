import java.util.Random;

public class getset {
    private int[] account = new int[10];

    public void setAccount() {
        Random r = new Random();
        for (int i = 0; i < 10; i++) {
            account[i] = (r.nextInt(10) + 1) * 1000;
        }
    }

    public int getBalance(int n) {
        return account[n];
    }
}
