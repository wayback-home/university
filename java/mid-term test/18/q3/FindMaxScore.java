import java.util.Random;

public class FindMaxScore {
    private int[] scores;

    public FindMaxScore() {
        scores = new int[10];
        Random random = new Random();

        for (int i = 0; i < scores.length; i++) {
            scores[i] = random.nextInt(101);
        }
    }

    public int findMaxScore() {
        int maxIdx = 0;
        for (int i = 1; i < scores.length; i++) {
            if (scores[maxIdx] < scores[i]) {
                maxIdx = i;
            }
        }
        return scores[maxIdx];
    }

    public static void main(String[] args) {
        FindMaxScore maxScore = new FindMaxScore();
        System.out.println("Max Score : " + maxScore.findMaxScore());
    }
}
