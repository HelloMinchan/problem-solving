import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        Map<String, Integer> numberDict = new HashMap<>();

        st = new StringTokenizer(br.readLine());
        while (n-- != 0) {
            String number = st.nextToken();

            if (numberDict.containsKey(number)) {
                numberDict.put(number, numberDict.get(number) + 1);
            } else {
                numberDict.put(number, 1);
            }
        }

        int m = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());
        while (m-- != 0) {
            String number = st.nextToken();

            if (numberDict.containsKey(number)) {
                bw.write(numberDict.get(number) + " ");
            } else {
                bw.write("0 ");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}