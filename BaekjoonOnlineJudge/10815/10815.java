import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        Set<Integer> cards = new HashSet<>();

        st = new StringTokenizer(br.readLine());
        while (n-- != 0) {
            cards.add(Integer.parseInt(st.nextToken()));
        }

        int m = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        while (m-- != 0) {
            if (cards.contains(Integer.parseInt(st.nextToken()))) {
                bw.write(1 + " ");
            } else {
                bw.write(0 + " ");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}