import java.io.*;
import java.util.*;

class Coordinate {

    int i;
    int j;

    Coordinate(int i, int j) {
        this.i = i;
        this.j = j;
    }
}

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;
    private static int n, m, k;
    private static int[][] board;
    private static boolean[][] visit;
    private static final int[] DX = {0, 0, -1, 1};
    private static final int[] DY = {-1, 1, 0, 0};
    private static final int WAY_COUNT = 4;

    private static int bfs(int startI, int startJ) {
        int divisionArea = 0;
        Queue<Coordinate> queue = new LinkedList<>();
        visit[startI][startJ] = true;
        queue.add(new Coordinate(startI, startJ));

        while (!queue.isEmpty()) {
            Coordinate coordinate = queue.poll();
            divisionArea++;

            for (int way = 0; way < WAY_COUNT; way++) {
                int nextI = coordinate.i + DX[way];
                int nextJ = coordinate.j + DY[way];

                if (nextI < 0 || nextI > n - 1 || nextJ < 0 || nextJ > m - 1) {
                    continue;
                }

                if (board[nextI][nextJ] == 0 && !visit[nextI][nextJ]) {
                    visit[nextI][nextJ] = true;
                    queue.add(new Coordinate(nextI, nextJ));
                }
            }
        }

        return divisionArea;
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        int divisionCount = 0;
        ArrayList<Integer> divisionAreas = new ArrayList<>();

        board = new int[n][m];
        visit = new boolean[n][m];

        while (k-- != 0) {
            st = new StringTokenizer(br.readLine());

            int underX = Integer.parseInt(st.nextToken());
            int underY = Integer.parseInt(st.nextToken());
            int upperX = Integer.parseInt(st.nextToken());
            int upperY = Integer.parseInt(st.nextToken());

            for (int i = n - upperY; i < n - underY; i++) {
                for (int j = underX; j < upperX; j++) {
                    board[i][j] = 1;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 0 && !visit[i][j]) {
                    divisionCount++;
                    divisionAreas.add(bfs(i, j));
                }
            }
        }

        bw.write(divisionCount + "\n");
        divisionAreas.stream().sorted().forEach(divisionArea -> {
            try {
                bw.write(divisionArea + " ");
            } catch (IOException e) {
            }
        });

        bw.flush();
        bw.close();
        br.close();
    }
}