import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static int n, m;
    private static int[][] adjacentMatrix;

    private static void floydWarShall() {
        for (int k = 1; k < n + 1; k++) {
            for (int i = 1; i < n + 1; i++) {
                for (int j = 1; j < n + 1; j++) {
                    if (adjacentMatrix[i][k] != 0 && adjacentMatrix[k][j] != 0) {
                        adjacentMatrix[i][j] = 1;
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        adjacentMatrix = new int[n + 1][n + 1];

        while (m-- != 0) {
            st = new StringTokenizer(br.readLine());

            int startVertex = Integer.parseInt(st.nextToken());
            int endVertex = Integer.parseInt(st.nextToken());

            adjacentMatrix[startVertex][endVertex] = 1;
        }

        floydWarShall();

        for (int i = 1; i < n + 1; i++) {
            int answer = 0;

            for (int j = 1; j < n + 1; j++) {
                if (i != j && adjacentMatrix[i][j] == 0 && adjacentMatrix[j][i] == 0) {
                    answer++;
                }
            }

            bw.write(answer + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}