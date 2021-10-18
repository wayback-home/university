public class IdentifiedScore extends Score {
    private String name;

    public IdentifiedScore(int p) {
        set(0);
    }

    public void set(String n, int p) {
        name = n;
        set(p);
    }

    public void set(String n) {
        name = n;
    }

    public String getName() {
        return name;
    }
}
