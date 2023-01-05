import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        Integer[] arrayA = new Integer[n];
        Integer[] arrayB = new Integer[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arrayA[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arrayB[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arrayA);
        Arrays.sort(arrayB, Collections.reverseOrder());

        int sum = 0;

        for (int i = 0; i < n; i++) {
            sum += arrayA[i] * arrayB[i];
        }

        bw.write(String.valueOf(sum));

        bw.flush();
        bw.close();
        br.close();
    }
}