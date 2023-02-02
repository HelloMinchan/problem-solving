import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());

        int[] array = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int answer = Integer.MAX_VALUE;
        int pA = 0;
        int pB = 0;
        int sum = array[0];

        while (true) {
            if (sum == s) {
                answer = Math.min(answer, pB - pA + 1);

                pA++;
                if (pA == n) {
                    break;
                }

                pB = pA;
                sum = array[pA];
            } else if (sum > s) {
                answer = Math.min(answer, pB - pA + 1);

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

        if (answer == Integer.MAX_VALUE) {
            bw.write("0");
        } else {
            bw.write(String.valueOf(answer));
        }

        bw.flush();
        bw.close();
        br.close();
    }
}