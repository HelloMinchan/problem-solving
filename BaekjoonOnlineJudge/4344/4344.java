import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int testCase = Integer.parseInt(br.readLine());

        while (testCase-- != 0) {
            st = new StringTokenizer(br.readLine());

            int count = Integer.parseInt(st.nextToken());
            ArrayList<Integer> scores = new ArrayList<Integer>();

            for (int i = 0; i < count; i++) {
                scores.add(Integer.parseInt(st.nextToken()));
            }

            double avg = scores.stream().mapToInt(Integer::intValue).average().getAsDouble();

            int upperAvgCount = (int) scores.stream().filter(score -> score > avg).count();

            bw.write(String.format("%.3f%%\n", (double) upperAvgCount / scores.size() * 100));
        }

        bw.flush();
        bw.close();
        br.close();
    }
}