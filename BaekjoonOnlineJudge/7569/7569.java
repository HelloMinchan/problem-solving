import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

class Tuple {

    int k;
    int i;
    int j;

    Tuple(int k, int i, int j) {
        this.k = k;
        this.i = i;
        this.j = j;
    }
}

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;
    private static int n, m, h;
    private static int[][][] box;
    private static int unripeCount = 0;
    private static Queue<Tuple> queue = new LinkedList<>();
    private static int answer = -1;
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};
    private static int[] dz = {-1, 1};

    public static void bfs() {
        while (!queue.isEmpty()) {
            int queueSize = queue.size();
            answer++;

            for (int cycle = 0; cycle < queueSize; cycle++) {
                Tuple tuple = queue.poll();

                for (int way = 0; way < 4; way++) {
                    int nextI = tuple.i + dx[way];
                    int nextJ = tuple.j + dy[way];

                    if (nextI < 0 || nextI > n - 1 || nextJ < 0 || nextJ > m - 1) {
                        continue;
                    }

                    if (box[tuple.k][nextI][nextJ] == 0) {
                        box[tuple.k][nextI][nextJ] = 1;
                        unripeCount--;
                        queue.add(new Tuple(tuple.k, nextI, nextJ));
                    }
                }

                for (int way = 0; way < 2; way++) {
                    int nextK = tuple.k + dz[way];

                    if (nextK < 0 || nextK > h - 1) {
                        continue;
                    }

                    if (box[nextK][tuple.i][tuple.j] == 0) {
                        box[nextK][tuple.i][tuple.j] = 1;
                        unripeCount--;
                        queue.add(new Tuple(nextK, tuple.i, tuple.j));
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        box = new int[h][n][m];

        for (int k = 0; k < h; k++) {
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());

                for (int j = 0; j < m; j++) {
                    box[k][i][j] = Integer.parseInt(st.nextToken());

                    if (box[k][i][j] == 0) {
                        unripeCount++;
                    } else if (box[k][i][j] == 1) {
                        queue.add(new Tuple(k, i, j));
                    }
                }
            }
        }

        bfs();

        if (unripeCount == 0) {
            bw.write(String.valueOf(answer));

        } else {
            bw.write("-1");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}