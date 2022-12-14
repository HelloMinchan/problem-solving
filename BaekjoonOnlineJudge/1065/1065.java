import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static boolean isHanNumber(int number) {
        String strNumber = String.valueOf(number);

        if (strNumber.length() != 1) {
            int diff = Character.getNumericValue(strNumber.charAt(0)) - Character.getNumericValue(
                strNumber.charAt(1));

            for (int index = 1; index < strNumber.length() - 1; index++) {
                if (diff != Character.getNumericValue(strNumber.charAt(index))
                    - Character.getNumericValue(
                    strNumber.charAt(index + 1))) {
                    return false;
                }
            }
        }

        return true;
    }

    public static void main(String[] args) throws IOException {
        int maxNumber = Integer.parseInt(br.readLine());
        int answer = 0;

        for (int number = 1; number <= maxNumber; number++) {
            if (isHanNumber(number)) {
                answer++;
            }
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}