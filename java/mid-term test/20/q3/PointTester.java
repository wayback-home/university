public class PointTester {
    public static void main(String[] argv) {
        Point point = Point.makePoint(10, 5);
        Point p2;
        System.out.println("X=" + point.getX() + "\tY=" + point.getY());
        p2 = point.get();
        System.out.println("X=" + p2.getX() + "\tY=" + p2.getY());
    }
}