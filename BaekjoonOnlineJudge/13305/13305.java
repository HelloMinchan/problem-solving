import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        Queue<Integer> roads = new LinkedList<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n - 1; i++) {
            roads.add(Integer.parseInt(st.nextToken()));
        }

        int[] prices = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            prices[i] = Integer.parseInt(st.nextToken());
        }

        long answer = 0;
        int car = 1;
        int oilbank = 0;
        int roadLength = roads.poll();
        boolean isPay = false;

        while (car != n - 1) {
            if (prices[oilbank] > prices[car]) {
                answer += (long) prices[oilbank] * roadLength;
                roadLength = 0;
                oilbank = car;
                isPay = true;
            }

            isPay = false;
            roadLength += roads.poll();
            car++;
        }

        if (!isPay) {
            answer += (long) prices[oilbank] * roadLength;
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}