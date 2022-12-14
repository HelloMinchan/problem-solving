import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        String word = br.readLine();
        Map<Character, Integer> alphaDict = new HashMap<Character, Integer>();

        for (int index = 0; index < word.length(); index++) {
            char alphabet = word.charAt(index);

            if (!alphaDict.containsKey(alphabet)) {
                alphaDict.put(alphabet, index);
            }
        }

        for (int alphabet = (int) 'a'; alphabet <= (int) 'z'; alphabet++) {
            if (alphaDict.containsKey((char) alphabet)) {
                bw.write(alphaDict.get((char) alphabet) + " ");
            } else {
                bw.write(-1 + " ");
            }

        }

        bw.flush();
        bw.close();
        br.close();
    }
}