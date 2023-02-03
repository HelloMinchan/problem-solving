import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        final int MAX_LENGTH = n + 1;

        int[] prefixSum = new int[MAX_LENGTH];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < MAX_LENGTH; i++) {
            prefixSum[i] = prefixSum[i - 1] + Integer.parseInt(st.nextToken());
        }

        HashMap<Integer, Integer> map = new HashMap<>();

        long answer = 0;

        for (int i = 1; i < MAX_LENGTH; i++) {
            if (prefixSum[i] == k) {
                answer++;
            }

            answer += map.getOrDefault(prefixSum[i] - k, 0);
            map.put(prefixSum[i], map.getOrDefault(prefixSum[i], 0) + 1);
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}