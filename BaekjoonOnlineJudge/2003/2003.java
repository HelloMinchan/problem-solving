import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int answer = 0;
        int sum = array[0];
        int pA = 0;
        int pB = 0;

        while (true) {
            if (sum == m) {
                answer++;

                pA++;
                if (pA == n) {
                    break;
                }

                pB = pA;
                sum = array[pA];
            } else if (sum > m) {
                sum -= array[pA];
                pA++;
            } else {
                pB++;
                if (pB == n) {
                    break;
                }

                sum += array[pB];
            }
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}