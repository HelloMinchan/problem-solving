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

    private static final int ALARM_DIFF = 45;
    private static final int FULL_MINUTE = 60;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        int hour = Integer.parseInt(st.nextToken());
        int minute = Integer.parseInt(st.nextToken());

        minute -= ALARM_DIFF;

        if (minute < 0) {
            hour--;
            minute = FULL_MINUTE + minute;
        }
        if (hour < 0) {
            hour = 23;
        }

        bw.write(hour + " " + minute);

        bw.flush();
        bw.close();
        br.close();
    }
}