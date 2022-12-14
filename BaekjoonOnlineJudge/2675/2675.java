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
            int repeatCount = Integer.parseInt(st.nextToken());
            String string = st.nextToken();

            StringBuilder answer = new StringBuilder();

            for (int index = 0; index < string.length(); index++) {
                for (int repeat = 0; repeat < repeatCount; repeat++) {
                    answer.append(string.charAt(index));
                }
            }

            bw.write(answer + "\n");
        }
        
        bw.flush();
        bw.close();
        br.close();
    }
}