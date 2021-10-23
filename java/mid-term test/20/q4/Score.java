public class Score {
    int point;

    public Score(int p) {
        point = p;
    }

    public int get() {
        return point;
    }

    public void set(int p) {
        point = p;
    }

    public boolean gt(Score p) {
        return this.point > p.get();
    }

    public boolean eq(Score p) {
        return this.point == p.get();
    }
}
