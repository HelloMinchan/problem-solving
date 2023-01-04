import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static int n;
    private static boolean[] colCheck;
    private static boolean[] slashCheck;
    private static boolean[] reverseSlashCheck;
    private static int answer = 0;

    private static void is_possible(int startI) {
        if (startI >= n) {
            answer++;
            return;
        }

        for (int j = 0; j < n; j++) {
            if (!colCheck[j] && !slashCheck[startI + j] && !reverseSlashCheck[startI - j + n - 1]) {
                colCheck[j] = true;
                slashCheck[startI + j] = true;
                reverseSlashCheck[startI - j + n - 1] = true;
                is_possible(startI + 1);
                colCheck[j] = false;
                slashCheck[startI + j] = false;
                reverseSlashCheck[startI - j + n - 1] = false;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        colCheck = new boolean[n];
        slashCheck = new boolean[n * 2 - 1];
        reverseSlashCheck = new boolean[n * 2 - 1];

        is_possible(0);

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}