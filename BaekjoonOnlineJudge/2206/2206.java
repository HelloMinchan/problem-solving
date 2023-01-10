import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

class Tuple implements Comparable<Tuple> {

    int i;
    int j;
    int distance;
    boolean brokenWall;

    Tuple(int i, int j, int distance, boolean brokenWall) {
        this.i = i;
        this.j = j;
        this.distance = distance;
        this.brokenWall = brokenWall;
    }

    @Override
    public int compareTo(Tuple target) {
        if (this.distance < target.distance) {
            return -1;
        } else if (this.distance == target.distance) {
            return -1;
        } else {
            return 1;
        }
    }
}

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;
    private static int n, m;
    private static int[][] map;
    private static boolean[][][] visit;
    private static final int WAY_COUNT = 4;
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};

    private static int bfs() {
        PriorityQueue<Tuple> queue = new PriorityQueue<>();
        queue.add(new Tuple(0, 0, 1, false));
        visit[0][0][0] = true;
        visit[1][0][0] = true;

        while (!queue.isEmpty()) {
            Tuple tuple = queue.poll();

            if (tuple.i == n - 1 && tuple.j == m - 1) {
                return tuple.distance;
            }

            for (int way = 0; way < WAY_COUNT; way++) {
                int nextI = tuple.i + dx[way];
                int nextJ = tuple.j + dy[way];

                if (nextI < 0 || nextI > n - 1 || nextJ < 0 || nextJ > m - 1) {
                    continue;
                }

                if (map[nextI][nextJ] == 1) {
                    if (!tuple.brokenWall) {
                        visit[1][nextI][nextJ] = true;
                        queue.add(new Tuple(nextI, nextJ, tuple.distance + 1, true));
                    }
                } else {
                    if (!tuple.brokenWall && !visit[0][nextI][nextJ]) {
                        visit[0][nextI][nextJ] = true;
                        queue.add(new Tuple(nextI, nextJ, tuple.distance + 1, tuple.brokenWall));
                    } else if (tuple.brokenWall && !visit[1][nextI][nextJ]) {
                        visit[1][nextI][nextJ] = true;
                        queue.add(new Tuple(nextI, nextJ, tuple.distance + 1, tuple.brokenWall));
                    }
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        visit = new boolean[2][n][m];

        for (int i = 0; i < n; i++) {
            String row = br.readLine();

            for (int j = 0; j < m; j++) {
                map[i][j] = Character.getNumericValue(row.charAt(j));
            }
        }

        bw.write(String.valueOf(bfs()));

        bw.flush();
        bw.close();
        br.close();
    }
}