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
        Point p = new Point(this.x, this.y);
        return p;
    }

    public static Point makePoint(int x, int y) {
        Point rt = new Point(x, y);
        return rt;
    }

}
