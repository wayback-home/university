public class Score {

    static int point;

    public static void setPoint(int p) {
        point = p;
    }

    public static int getPoint() {
        return point;
    }

    public static void main(String[] args) {
        setPoint(80);
        System.out.println(getPoint());
        setPoint(85);
        System.out.println(getPoint());
    }
}