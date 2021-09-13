import java.util.Scanner;

public class practice3 {

    public static void main(String[] args) {
        Scanner getNum = new Scanner(System.in);
        System.out.println("수를 입력하세요 : ");

        int[] sum = new int[10];
        for (int i = 0; i < 10; i++) {
            int Num = getNum.nextInt();
            if (Num <= 100 && Num >= 0) {
                sum[i] += Num;
            } else {
                System.out.println("범위 초과");
                i -= 1;
            }
        }
        int sumArray = 0;
        for (int j = 0; j < sum.length; j++) {
            sumArray += sum[j];
        }
        int avgArray = 0;
        avgArray = sumArray / sum.length;

        System.out.println("평균값 = " + avgArray);

    }
}
