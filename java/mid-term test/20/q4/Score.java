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

    public boolean gt(Score name) {
        return point > name.get();
    }

    public boolean eq(Score name) {
        return point == name.get();
    }
}
