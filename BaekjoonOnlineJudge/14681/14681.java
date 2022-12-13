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
        int x = Integer.parseInt(br.readLine());
        int y = Integer.parseInt(br.readLine());

        if (x > 0 && y > 0) {
            bw.write("1");
        } else if (x > 0 && y < 0) {
            bw.write("4");
        } else if (x < 0 && y > 0) {
            bw.write("2");
        } else {
            bw.write("3");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}