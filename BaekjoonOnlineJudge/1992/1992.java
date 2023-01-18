import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static int n;
    private static int[][] picture;
    private static StringBuilder sb;

    private static boolean getCompressResult(int startI, int startJ, int size) {
        for (int i = startI; i < startI + size; i++) {
            for (int j = startJ; j < startJ + size; j++) {
                if (picture[i][j] != picture[startI][startJ]) {
                    return false;
                }
            }
        }

        return true;
    }

    private static void dfs(int startI, int startJ, int size) {
        if (getCompressResult(startI, startJ, size)) {
            sb.append(picture[startI][startJ]);
            return;
        }

        int newSize = size / 2;
        sb.append("(");
        dfs(startI, startJ, newSize);
        dfs(startI, startJ + newSize, newSize);
        dfs(startI + newSize, startJ, newSize);
        dfs(startI + newSize, startJ + newSize, newSize);
        sb.append(")");
    }

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        picture = new int[n][n];
        sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            String row = br.readLine();

            for (int j = 0; j < n; j++) {
                picture[i][j] = Character.getNumericValue(row.charAt(j));
            }
        }

        dfs(0, 0, n);

        bw.write(sb.toString());

        bw.flush();
        bw.close();
        br.close();
    }
}