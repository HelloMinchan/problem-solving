import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> negativePq = new PriorityQueue<>((number1, number2) -> {
            return number2 - number1;
        });
        PriorityQueue<Integer> positivePq = new PriorityQueue<>((number1, number2) -> {
            return number1 - number2;
        });

        while (n-- != 0) {
            int x = Integer.parseInt(br.readLine());

            if (x == 0) {
                if (!negativePq.isEmpty() && !positivePq.isEmpty()) {
                    if (Math.abs(negativePq.peek()) > Math.abs(positivePq.peek())) {
                        bw.write(positivePq.poll() + "\n");
                    } else {
                        bw.write(negativePq.poll() + "\n");
                    }
                } else if (!negativePq.isEmpty()) {
                    bw.write(negativePq.poll() + "\n");
                } else if (!positivePq.isEmpty()) {
                    bw.write(positivePq.poll() + "\n");
                } else {
                    bw.write("0\n");
                }
            } else {
                if (x < 0) {
                    negativePq.add(x);
                } else {
                    positivePq.add(x);
                }
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}