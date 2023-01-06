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

        Queue<Integer> yosepus = new LinkedList<>();

        for (int number = 1; number < n + 1; number++) {
            yosepus.add(number);
        }

        Queue<Integer> answer = new LinkedList<>();

        while (!yosepus.isEmpty()) {
            for (int count = 0; count < k - 1; count++) {
                yosepus.add(yosepus.poll());
            }

            answer.add(yosepus.poll());
        }

        bw.write("<");
        while (n-- != 1) {
            bw.write(answer.poll() + ", ");
        }

        bw.write(answer.poll() + ">");

        bw.flush();
        bw.close();
        br.close();
    }
}