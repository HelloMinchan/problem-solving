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

    private static final int FULL_HOUR = 24;
    private static final int FULL_MINUTE = 60;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        int hour = Integer.parseInt(st.nextToken());
        int minute = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        int requireMinute = Integer.parseInt(st.nextToken());

        hour += (minute + requireMinute) / FULL_MINUTE;
        minute = (minute + requireMinute) % FULL_MINUTE;

        if (hour >= FULL_HOUR) {
            hour -= FULL_HOUR;
        }

        bw.write(hour + " " + minute);

        bw.flush();
        bw.close();
        br.close();
    }
}