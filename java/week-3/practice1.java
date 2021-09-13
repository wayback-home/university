import java.util.Scanner;

public class practice1 {
    public static void main(String[] args) {

        System.out.println("연도를 입력하세요");
        Scanner year = new Scanner(System.in);

        int getYear = year.nextInt();

        if (getYear % 4 == 0) {
            if (getYear % 100 == 0) {
                if (getYear % 400 == 0) {
                    System.out.println("윤년입니다.");
                } else {
                    System.out.println("윤년이 아닙니다.");
                }
            } else {
                System.out.println("윤년입니다.");
            }
        } else {
            System.out.println("윤년이 아닙니다.");
        }

    }
}
