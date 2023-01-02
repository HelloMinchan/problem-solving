import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int cardCount = Integer.parseInt(br.readLine());
        Set<Integer> cardDeck = new HashSet<>();

        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            cardDeck.add(Integer.parseInt(st.nextToken()));
        }

        int targetCardCount = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        while (st.hasMoreTokens()) {
            if (cardDeck.contains(Integer.parseInt(st.nextToken()))) {
                bw.write("1 ");
            } else {
                bw.write("0 ");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}