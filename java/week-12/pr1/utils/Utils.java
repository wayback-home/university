package utils;

import src.TdataReader;

public class Utils {
    public int findMax(TdataReader reader, int b, int e) {
        int max = b;

        for (int i = b; i < e; i++) {
            if (reader.isGreat(i, max)) {
                max = i;
            }
        }
        return max;
    }
}