import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;
    private static int k, n;
    private static int[] lanCables;

    private static long getLanCable(long length) {
        return Arrays.stream(lanCables).mapToLong(lanCable -> lanCable / length).sum();
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        k = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        lanCables = new int[k];

        for (int i = 0; i < k; i++) {
            lanCables[i] = Integer.parseInt(br.readLine());
        }

        long answer = 0;
        long left = 1;
        long right = Arrays.stream(lanCables).max().getAsInt();

        while (left <= right) {
            long mid = (left + right) / 2;

            int cutLanCable = (int) getLanCable(mid);

            if (cutLanCable < n) {
                right = mid - 1;
            } else {
                answer = Math.max(answer, mid);
                left = mid + 1;
            }
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}