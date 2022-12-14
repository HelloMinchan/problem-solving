import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        int reversedNumber1 = Integer.parseInt(
            new StringBuilder(st.nextToken()).reverse().toString());
        int reversedNumber2 = Integer.parseInt(
            new StringBuilder(st.nextToken()).reverse().toString());

        if (reversedNumber1 < reversedNumber2) {
            bw.write(String.valueOf(reversedNumber2));
        } else {
            bw.write(String.valueOf(reversedNumber1));
        }

        bw.flush();
        bw.close();
        br.close();
    }
}