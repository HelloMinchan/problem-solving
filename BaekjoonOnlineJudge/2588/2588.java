import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        int n1 = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        String n2 = st.nextToken();

        bw.write(n1 * Character.getNumericValue(n2.charAt(2)) + "\n");
        bw.write(n1 * Character.getNumericValue(n2.charAt(1)) + "\n");
        bw.write(n1 * Character.getNumericValue(n2.charAt(0)) + "\n");
        bw.write(n1 * Integer.parseInt(n2) + "\n");

        bw.flush();
        bw.close();
        br.close();
    }
}