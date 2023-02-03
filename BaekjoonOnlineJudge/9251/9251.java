import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        String string1 = "0" + br.readLine();
        String string2 = "0" + br.readLine();

        int[][] memoization = new int[string1.length()][string2.length()];

        for (int i = 1; i < string1.length(); i++) {
            for (int j = 1; j < string2.length(); j++) {
                if (string1.charAt(i) == string2.charAt(j)) {
                    memoization[i][j] = memoization[i - 1][j - 1] + 1;
                } else {
                    memoization[i][j] = Math.max(memoization[i - 1][j], memoization[i][j - 1]);
                }
            }
        }

        bw.write(String.valueOf(memoization[string1.length() - 1][string2.length() - 1]));

        bw.flush();
        bw.close();
        br.close();
    }
}