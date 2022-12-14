import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static int getScore(String result) {
        int answer = 0;
        int score = 0;

        for (int i = 0; i < result.length(); i++) {
            if (result.charAt(i) == 'O') {
                score++;
                answer += score;
            } else {
                score = 0;
            }
        }

        return answer;
    }

    public static void main(String[] args) throws IOException {
        int testCase = Integer.parseInt(br.readLine());

        while (testCase-- != 0) {
            bw.write(getScore(br.readLine()) + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}