import java.io.*;
import java.util.*;
import java.util.stream.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        int numberOfApplier = Integer.parseInt(st.nextToken());
        int numberOfWinner = Integer.parseInt(st.nextToken());

        Integer[] scores = new Integer[numberOfApplier];

        st = new StringTokenizer(br.readLine());

        int index = 0;
        while (st.hasMoreTokens()) {
            scores[index++] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(scores, Collections.reverseOrder());

        bw.write(String.valueOf(scores[numberOfWinner - 1]));

        bw.flush();
        bw.close();
        br.close();
    }
}