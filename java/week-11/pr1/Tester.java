import java.util.*;

import util.Algorithm;
import util.Compare;

public class Tester implements Compare {

    int[] data;

    public Tester() {
        Random rand = new Random();
        data = new int[5];
        for (int i = 0; i < data.length; i++) {
            data[i] = rand.nextInt(100);
        }
    }

    public int get(int idx) {
        return data[idx];
    }

    public static void main(String[] args) {
        Tester tester = new Tester();
        Algorithm al = new Algorithm();
        al.findMax(tester, 0, 4);

        System.out.println(tester.get(al.findMax(tester, 0, 4)));
    }

    @Override
    public boolean isGreater(int n, int m) {
        return data[n] > data[m];
    }
}
