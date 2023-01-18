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

        PriorityQueue<Long> pq = new PriorityQueue<>();

        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            pq.add(Long.parseLong(st.nextToken()));
        }

        while (m-- != 0) {
            long card1 = pq.poll();
            long card2 = pq.poll();

            pq.add(card1 + card2);
            pq.add(card1 + card2);
        }

        bw.write(String.valueOf(pq.stream().mapToLong(Long::valueOf).sum()));

        bw.flush();
        bw.close();
        br.close();
    }
}