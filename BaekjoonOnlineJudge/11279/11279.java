import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(Collections.reverseOrder());

        while (n-- != 0) {
            int number = Integer.parseInt(br.readLine());

            if (number == 0) {
                if (minHeap.size() != 0) {
                    bw.write(minHeap.poll() + "\n");
                } else {
                    bw.write(0 + "\n");
                }
            } else {
                minHeap.add(number);
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}