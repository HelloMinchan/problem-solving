import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static void setMatrix(int n, int m, int[][] matrix) throws IOException {
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                int element = Integer.parseInt(st.nextToken());

                matrix[i][j] = element;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] matrixA = new int[n][m];
        int[][] matrixB = new int[n][m];

        setMatrix(n, m, matrixA);
        setMatrix(n, m, matrixB);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                bw.write(matrixA[i][j] + matrixB[i][j] + " ");
            }
            bw.write("\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}