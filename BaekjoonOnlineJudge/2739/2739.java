import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        int number = Integer.parseInt(st.nextToken());

        for (int index = 1; index < 10; index++) {
            bw.write(String.format("%d * %d = %d", number, index, number * index) + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}