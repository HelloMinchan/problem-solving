import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static boolean isGroupWord(String word) {
        Map<Character, Boolean> visitDict = new HashMap<>();
        visitDict.put(word.charAt(0), true);

        for (int i = 1; i < word.length(); i++) {
            if (visitDict.containsKey(word.charAt(i))) {
                if (word.charAt(i) != word.charAt(i - 1)) {
                    return false;
                }
            } else {
                visitDict.put(word.charAt(i), true);
            }
        }

        return true;
    }

    public static void main(String[] args) throws IOException {
        int wordCount = Integer.parseInt(br.readLine());
        int answer = 0;

        while (wordCount-- != 0) {
            String word = br.readLine();

            if (isGroupWord(word)) {
                answer++;
            }
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}