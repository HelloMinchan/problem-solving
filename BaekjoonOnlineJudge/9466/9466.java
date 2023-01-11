import java.io.*;
import java.util.*;
import java.util.stream.Collectors;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;
    private static int n;
    private static int[] votes;
    private static boolean[] visit;
    private static boolean[] finishMatching;
    private static int matchingCount;

    private static void dfs(int person) {
        if (finishMatching[person]) {
            return;
        }

        if (visit[person]) {
            finishMatching[person] = true;
            matchingCount++;
        }

        visit[person] = true;
        dfs(votes[person]);
        finishMatching[person] = true;
        visit[person] = false;
    }


    public static void main(String[] args) throws IOException {
        int testCase = Integer.parseInt(br.readLine());

        while (testCase-- != 0) {
            n = Integer.parseInt(br.readLine());
            matchingCount = 0;
            votes = new int[n + 1];
            visit = new boolean[n + 1];
            finishMatching = new boolean[n + 1];

            st = new StringTokenizer(br.readLine());
            for (int i = 1; i < n + 1; i++) {
                votes[i] = Integer.parseInt(st.nextToken());
            }

            for (int person = 1; person < n + 1; person++) {
                if (!finishMatching[person]) {
                    dfs(person);
                }
            }

            bw.write(n - matchingCount + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}