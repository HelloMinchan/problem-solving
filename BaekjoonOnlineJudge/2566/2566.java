import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static final int LENGTH = 9;

    public static void main(String[] args) throws IOException {
        int answerValue = 0;
        int answerI = 0;
        int answerJ = 0;

        for (int i = 0; i < LENGTH; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < LENGTH; j++) {
                int value = Integer.parseInt(st.nextToken());

                if (answerValue <= value) {
                    answerValue = value;
                    answerI = i;
                    answerJ = j;
                }
            }
        }

        bw.write(answerValue + "\n");
        bw.write((answerI + 1) + " " + (answerJ + 1));

        bw.flush();
        bw.close();
        br.close();
    }
}