import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;
    private static int n, c;
    private static int[] coordinates;

    private static boolean getPossible(int distance) {
        int installCount = 1;
        int nextInstallDistance = coordinates[0] + distance;

        for (int i = 1; i < n; i++) {
            if (coordinates[i] >= nextInstallDistance) {
                nextInstallDistance = coordinates[i] + distance;
                installCount++;
            }
        }

        if (installCount >= c) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        coordinates = new int[n];
        for (int i = 0; i < n; i++) {
            coordinates[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(coordinates);

        int answer = 0;
        int left = 1;
        int right = Arrays.stream(coordinates).max().getAsInt();

        while (left <= right) {
            int mid = (left + right) / 2;

            if (getPossible(mid)) {
                answer = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}