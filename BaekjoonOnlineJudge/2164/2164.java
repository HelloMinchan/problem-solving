import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        Queue<Integer> queue = new LinkedList<>();
        int n = Integer.parseInt(br.readLine());

        for (int number = 1; number <= n; number++) {
            queue.add(number);
        }

        while (queue.size() != 1) {
            queue.remove();
            int number = queue.poll();
            queue.add(number);
        }

        bw.write(String.valueOf(queue.peek()));

        bw.flush();
        bw.close();
        br.close();
    }
}