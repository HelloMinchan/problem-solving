import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int number = Integer.parseInt(br.readLine());

        for (int i = 1; i <= number; i++) {
            StringBuilder starLine = new StringBuilder();

            for (int k = number - i; k > 0; k--) {
                starLine.append(" ");
            }
            for (int j = 1; j <= i; j++) {
                starLine.append("*");
            }

            bw.write(starLine + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}