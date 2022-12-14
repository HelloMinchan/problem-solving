import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        for (int index = 0; index < n; index++) {
            int number = Integer.parseInt(st.nextToken());

            if (number < x) {
                bw.write(number + " ");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}