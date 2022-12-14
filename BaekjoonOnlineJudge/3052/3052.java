import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static final int MAX_COUNT = 10;
    private static final int DIVIDER = 42;


    public static void main(String[] args) throws IOException {
        Set<Integer> remainders = new HashSet<Integer>();

        for (int i = 0; i < MAX_COUNT; i++) {
            remainders.add(Integer.parseInt(br.readLine()) % DIVIDER);
        }

        bw.write(String.valueOf(remainders.size()));

        bw.flush();
        bw.close();
        br.close();
    }
}