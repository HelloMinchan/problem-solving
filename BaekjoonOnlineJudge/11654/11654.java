import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        char ascii = br.readLine().charAt(0);

        bw.write(String.valueOf((int) ascii));

        bw.flush();
        bw.close();
        br.close();
    }
}