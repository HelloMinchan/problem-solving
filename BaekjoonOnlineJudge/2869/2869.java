import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;
    private static int upMeter, downMeter, v;

    private static boolean getPossible(long day) {
        long height = (upMeter - downMeter) * (day - 1) + upMeter;

        if (height >= v) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        upMeter = Integer.parseInt(st.nextToken());
        downMeter = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());

        long answer = 0;
        long left = 1;
        long right = v;

        while (left <= right) {
            long mid = (left + right) / 2;

            if (getPossible(mid)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}