package src;

import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

import utils.Compare;
import utils.Utils;

public class TdataReader implements Compare {
	private int[] data;

	public TdataReader() {
		data = new int[100];

		try {
			DataInputStream in = new DataInputStream(new FileInputStream("tdata.dat"));

			for (int i = 0; i < 100; i++) {
				data[i] = in.readInt();
			}

			in.close();

		} catch (FileNotFoundException e) {

			e.printStackTrace();
		} catch (IOException e) {

			e.printStackTrace();
		}
	}

	public int get(int n) {
		return data[n];
	}

	public static void main(String[] args) {

		TdataReader reader = new TdataReader();
		Utils algorythm = new Utils();

		System.out.println(algorythm.findMax(reader, 0, 100));

		int i = algorythm.findMax(reader, 0, 100);

		System.out.println(reader.get(i));

	}

	@Override
	public boolean isGreat(int n, int m) {
		return data[n] > data[m];
	}

}
