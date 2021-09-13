import java.util.Scanner;

public class practice2 {

    public static void main(String[] args) {
        Scanner getNum = new Scanner(System.in);
        System.out.println("수를 입력하세요 : ");

        int sum = 0;
        for (int i = 0; i <= 9; i++) {
            int Num = getNum.nextInt();
            if (Num <= 100 && Num >= 0) {
                sum += Num;
            } else {
                System.out.println("범위 초과");
                i -= 1;
            }
        }
        int avg = sum / 10;
        System.out.println("평균값 = " + avg);
    }
}
