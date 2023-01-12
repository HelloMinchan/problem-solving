import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        String[] numbers = new String[k];
        int maxNumber = 0;
        for (int i = 0; i < k; i++) {
            numbers[i] = br.readLine();
            maxNumber = Math.max(maxNumber, Integer.parseInt(numbers[i]));
        }

        Arrays.sort(numbers, (number1, number2) -> {
            String temp = number2 + number1;
            return temp.compareTo(number1 + number2);
        });

        String answer = "";
        boolean isOverlap = false;
        for (int i = 0; i < k; i++) {
            answer += numbers[i];

            if (maxNumber == Integer.parseInt(numbers[i]) && isOverlap == false) {
                isOverlap = true;

                for (int j = 0; j < n - k; j++) {
                    answer += numbers[i];
                }
            }
        }

        bw.write(answer);

        bw.flush();
        bw.close();
        br.close();
    }
}