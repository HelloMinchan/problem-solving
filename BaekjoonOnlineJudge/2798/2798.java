import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static final int MAX_PICK_COUNT = 3;
    private static int answer = 0;
    private static Stack<Integer> cardStack = new Stack<>();

    private static void getBlackJack(final int NUMBER_OF_CARD, final int MAX_SUM,
        int selectCardIndex, int[] cards) {

        if (cardStack.size() == MAX_PICK_COUNT) {
            int sumOfCards = cardStack.stream().mapToInt(card -> card).sum();

            if (sumOfCards <= MAX_SUM && answer <= sumOfCards) {
                answer = sumOfCards;
            }

            return;
        }

        for (int index = selectCardIndex; index < NUMBER_OF_CARD; index++) {
            cardStack.add(cards[index]);
            getBlackJack(NUMBER_OF_CARD, MAX_SUM, index + 1, cards);
            cardStack.pop();
        }
    }


    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        final int NUMBER_OF_CARD = Integer.parseInt(st.nextToken());
        final int MAX_NUMBER = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] cards = new int[NUMBER_OF_CARD];

        int index = 0;
        while (st.hasMoreTokens()) {
            cards[index++] = Integer.parseInt(st.nextToken());
        }

        getBlackJack(NUMBER_OF_CARD, MAX_NUMBER, 0, cards);

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}