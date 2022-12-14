import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static final int maxCount = 9;


    public static void main(String[] args) throws IOException {
        ArrayList<Integer> numbers = new ArrayList<Integer>();

        for (int i = 0; i < maxCount; i++) {
            numbers.add(Integer.parseInt(br.readLine()));
        }

        int maxNumber = Collections.max(numbers);
        bw.write(maxNumber + "\n");
        bw.write(String.valueOf(numbers.indexOf(maxNumber) + 1));

        bw.flush();
        bw.close();
        br.close();
    }
}