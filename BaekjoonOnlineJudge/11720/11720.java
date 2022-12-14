import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int count = Integer.parseInt(br.readLine());
        String numbers = br.readLine();
        int answer = 0;

        for (int index = 0; index < numbers.length(); index++) {
            answer += Character.getNumericValue(numbers.charAt(index));
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}