import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int count = Integer.parseInt(br.readLine());
        int[] numbers = new int[count];

        st = new StringTokenizer(br.readLine());

        for (int index = 0; index < count; index++) {
            numbers[index] = Integer.parseInt(st.nextToken());
        }

        int targetNumber = Integer.parseInt(br.readLine());

        int answer = 0;

        for (int number : numbers) {
            if (number == targetNumber) {
                answer++;
            }
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}