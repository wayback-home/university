public class Tester {
    public static void main(String[] args) {
        Counter c = new Counter();
        Counter c1 = new Counter();
        Counter c2 = new Counter();

        // ! c.run(); <-- Thread를 이용하여 실행하는것이 아님
        c.start(); // <-- 옳은 방법

        c1.start();
        c2.start();
    }
}
