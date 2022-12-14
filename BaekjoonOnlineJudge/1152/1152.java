import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        bw.write(String.valueOf(
            Arrays.stream(br.readLine().strip().split(" ")).filter(word -> word != "").count()));

        bw.flush();
        bw.close();
        br.close();
    }
}