import java.util.Scanner;

public class TenData {
    private int total;

    public void dataProcess() {
        int n;
        int count = 0;
        Scanner scanner = new Scanner(System.in);
        total = 0;
        while (count < 10) {
            System.out.println("input data (between 0 and 100) : ");
            n = scanner.nextInt();
            if (n < 0 || n > 100) {
                System.out.println("Wrong data (0 <= data <= 100)");
            } else {
                count++;
                total = total + n;
            }
        }
        System.out.println("Average : " + total / 10);
    }

    public static void main(String[] args) {
        TenData tenData = new TenData();
        tenData.dataProcess();
    }
}