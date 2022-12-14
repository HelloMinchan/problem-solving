import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static final int ONE_HUNDRED = 100;

    public static void main(String[] args) throws IOException {
        int count = Integer.parseInt(br.readLine());
        ArrayList<Integer> scores = new ArrayList<Integer>();

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < count; i++) {
            scores.add(Integer.parseInt(st.nextToken()));
        }

        int maxScore = Collections.max(scores);

        int[] scoresArray = scores.stream().mapToInt(Integer::intValue).toArray();

        bw.write(String.valueOf(
            Arrays.stream(scoresArray).mapToDouble(score -> (double) score / maxScore * ONE_HUNDRED)
                .average()
                .getAsDouble()));

        bw.flush();
        bw.close();
        br.close();
    }
}