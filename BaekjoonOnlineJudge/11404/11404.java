import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static int n, m;
    private static long[][] adjacentMatrix;
    private static final int INF = Integer.MAX_VALUE;

    private static void floydWarShall() {
        for (int k = 1; k < n + 1; k++) {
            for (int i = 1; i < n + 1; i++) {
                for (int j = 1; j < n + 1; j++) {
                    adjacentMatrix[i][j] = Math.min(adjacentMatrix[i][j],
                        adjacentMatrix[i][k] + adjacentMatrix[k][j]);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        adjacentMatrix = new long[n + 1][n + 1];

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (i == j) {
                    adjacentMatrix[i][j] = 0;
                } else {

                    adjacentMatrix[i][j] = INF;
                }
            }
        }

        while (m-- != 0) {
            st = new StringTokenizer(br.readLine());

            int startVertex = Integer.parseInt(st.nextToken());
            int endVertex = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            adjacentMatrix[startVertex][endVertex] = Math.min(
                adjacentMatrix[startVertex][endVertex], weight);
        }

        floydWarShall();

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (adjacentMatrix[i][j] == INF) {
                    bw.write("0 ");
                } else {

                    bw.write(adjacentMatrix[i][j] + " ");
                }
            }
            bw.write("\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}