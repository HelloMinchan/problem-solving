import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        String string;
        
        while ((string = br.readLine()) != null) {
            st = new StringTokenizer(string);

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (a + b == 0) {
                break;
            } else {
                bw.write(a + b + "\n");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}