public class ScoreTest {
    public static void main(String[] args) {
        Score kim = new Score(100);
        try {
            kim.set(90);
        } catch (IllegalArgumentException e) {
            System.out.println("범위를 벗어난 점수 설정...");
        }
        kim.set(-90);
        System.out.println(kim.get());
    }
}
