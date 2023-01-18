import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        while (n-- != 0) {
            pq.add(Integer.parseInt(br.readLine()));
        }

        if (n == 1) {
            bw.write(String.valueOf(pq.poll()));
            return;
        }

        int answer = 0;
        while (pq.size() != 1) {
            int sum = pq.poll() + pq.poll();
            answer += sum;
            pq.add(sum);
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}