import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        String word = br.readLine().toUpperCase();

        Map<Character, Integer> alphaDict = new HashMap<Character, Integer>();

        for (int index = 0; index < word.length(); index++) {
            char alphabet = word.charAt(index);
            if (alphaDict.containsKey(alphabet)) {
                alphaDict.put(alphabet, alphaDict.get(alphabet) + 1);
            } else {
                alphaDict.put(alphabet, 1);
            }
        }

        int maxCount = Collections.max(alphaDict.values());
        ArrayList<Character> answer = new ArrayList<Character>();

        alphaDict.forEach((alphabet, count) -> {
            if (count == maxCount) {
                answer.add(alphabet);
            }
        });

        if (answer.size() > 1) {
            bw.write("?");
        } else {
            bw.write(String.valueOf(answer.get(0)));
        }

        bw.flush();
        bw.close();
        br.close();
    }
}