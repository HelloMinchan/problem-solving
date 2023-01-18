import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>((gift1, gift2) -> gift2 - gift1);

        while (n-- != 0) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            if (a != 0) {
                while (st.hasMoreTokens()) {
                    pq.add(Integer.parseInt(st.nextToken()));
                }
            } else {
                if (!pq.isEmpty()) {
                    bw.write(pq.poll() + "\n");
                } else {
                    bw.write("-1\n");
                }
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}