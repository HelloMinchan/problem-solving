import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        int number1 = Integer.parseInt(st.nextToken());
        int number2 = Integer.parseInt(st.nextToken());
        int number3 = Integer.parseInt(st.nextToken());

        if (number1 == number2 && number1 == number3) {
            bw.write(String.valueOf(10000 + (number1 * 1000)));
        } else if (number1 == number2) {
            bw.write(String.valueOf(1000 + (number1 * 100)));
        } else if (number1 == number3) {
            bw.write(String.valueOf(1000 + (number1 * 100)));
        } else if (number2 == number3) {
            bw.write(String.valueOf(1000 + (number2 * 100)));
        } else {
            List<Integer> numbers = List.of(number1, number2, number3);

            bw.write(String.valueOf(Collections.max(numbers) * 100));
        }

        bw.flush();
        bw.close();
        br.close();
    }
}