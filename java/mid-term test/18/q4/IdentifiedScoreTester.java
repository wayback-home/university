public class IdentifiedScoreTester {
    public static void main(String[] args) {
        IdentifiedScore hong = new IdentifiedScore(95);
        hong.set("Hong", 90);
        System.out.println(hong.getName() + " : " + hong.get());

        hong.set("GILDONG");
        hong.set(99);

        System.out.println(hong.getName() + " : " + hong.get());
    }
}
