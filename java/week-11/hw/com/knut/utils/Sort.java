package com.knut.utils;

public class Sort implements Compare {
    private int data1, data2;

    @Override
    public boolean isGreat(int n, int m) {
        return data1 > data2;
    }

    @Override
    public void swap(int n, int m) {
        int temp;
        for (int i = 0; i < 10; i++) {

            if (isGreat(i, i + 1) == true) {
                temp = data2;
                data2 = data1;
                data1 = temp;
            }
        }
    }
}
