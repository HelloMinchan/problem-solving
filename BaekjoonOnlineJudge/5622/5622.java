import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        String word = br.readLine();
        Map<Character, Integer> phone = new HashMap<Character, Integer>();
        int answer = 0;

        phone.put('A', 3);
        phone.put('B', 3);
        phone.put('C', 3);
        phone.put('D', 4);
        phone.put('E', 4);
        phone.put('F', 4);
        phone.put('G', 5);
        phone.put('H', 5);
        phone.put('I', 5);
        phone.put('J', 6);
        phone.put('K', 6);
        phone.put('L', 6);
        phone.put('M', 7);
        phone.put('N', 7);
        phone.put('O', 7);
        phone.put('P', 8);
        phone.put('Q', 8);
        phone.put('R', 8);
        phone.put('S', 8);
        phone.put('T', 9);
        phone.put('U', 9);
        phone.put('V', 9);
        phone.put('W', 10);
        phone.put('X', 10);
        phone.put('Y', 10);
        phone.put('Z', 10);

        for (int index = 0; index < word.length(); index++) {
            answer += phone.get(word.charAt(index));
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}