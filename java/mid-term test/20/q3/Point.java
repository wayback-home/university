public class Point {
    int x, y;

    public Point() {
        this(0, 0);

    }

    public Point(int x, int y) {
        this.x = x;
        this.y = y;

    }

    public void set(int x, int y) {
        this.x = x;
        this.y = y;

    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public Point get() {
        return new Point(x, y);
    }

    public static Point makePoint(int x, int y) {
        return new Point(x, y);
    }

}
