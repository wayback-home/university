import java.util.Scanner;

public class HelloWorld {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n;

        System.out.println("정수를 입력하시오 : ");
        n = in.nextInt();

        if (isEven(n)) {
            System.out.println("짝수");
        } else {
            System.out.println("홀수");
        }

    }

    public static boolean isEven(int n) {
        return n % 2 == 0;
    }
}
