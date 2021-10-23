public class ScoreTester {
    public static void main(String[] args) {
        Score kim = new Score(94);
        Score lee = new Score(93);
        Score hong = new Score(94);

        System.out.println(kim.get());
        System.out.println(kim.gt(lee));
        System.out.println(kim.eq(hong));
        System.out.println(kim.eq(lee));
    }
}
