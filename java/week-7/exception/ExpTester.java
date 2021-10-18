public class ExpTester {
    public double div(int n1, int n2) throws ArithmeticException {
        int res;
        res = n1 / n2;
        return res;
    }

    public static void main(String[] args) {
        ExpTester obj = new ExpTester();

        try {
            System.out.println(obj.div(12, 0));
        } catch (ArithmeticException e) {
            System.out.println("0 나눔 오류");
        }
    }
}
