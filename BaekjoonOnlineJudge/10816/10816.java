import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        Map<Integer, Integer> cards = new HashMap<>();

        st = new StringTokenizer(br.readLine());
        while (n-- != 0) {
            int card = Integer.parseInt(st.nextToken());

            if (cards.containsKey(card)) {
                cards.put(card, cards.get(card) + 1);
            } else {
                cards.put(card, 1);
            }
        }

        int m = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        while (m-- != 0) {
            int card = Integer.parseInt(st.nextToken());

            if (cards.containsKey(card)) {
                bw.write(cards.get(card) + " ");
            } else {
                bw.write(0 + " ");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}