import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int year = Integer.parseInt(st.nextToken());

        if (year % 4 == 0) {
            if (year % 100 != 0 || year % 400 == 0) {
                bw.write("1");
            } else {
                bw.write("0");
            }
        } else {
            bw.write("0");
        }
        
        bw.flush();
        bw.close();
        br.close();
    }
}