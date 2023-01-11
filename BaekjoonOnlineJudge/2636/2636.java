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
    private static int n;
    private static int m;
    private static int[][] box;
    private static boolean[][] airVisit;
    private static boolean[][] cheeseVisit;
    private static final int[] DX = {0, 0, -1, 1};
    private static final int[] DY = {-1, 1, 0, 0};
    private static final int WAY_COUNT = 4;
    private static final Queue<Coordinate> AIR_QUEUE = new LinkedList<>();
    private static final Queue<Coordinate> CHEESE_QUEUE = new LinkedList<>();
    private static int hour = 0;
    private static int remainCheeses = 0;

    private static void getMeltingCheeses() {
        while (!AIR_QUEUE.isEmpty()) {
            Coordinate air = AIR_QUEUE.poll();

            for (int way = 0; way < WAY_COUNT; way++) {
                int nextI = air.i + DX[way];
                int nextJ = air.j + DY[way];

                if (nextI < 0 || nextI > n - 1 || nextJ < 0 || nextJ > m - 1) {
                    continue;
                }

                if (box[nextI][nextJ] == 0) {
                    if (!airVisit[nextI][nextJ]) {
                        airVisit[nextI][nextJ] = true;
                        AIR_QUEUE.add(new Coordinate(nextI, nextJ));
                    }
                } else {
                    if (!cheeseVisit[nextI][nextJ]) {
                        cheeseVisit[nextI][nextJ] = true;
                        CHEESE_QUEUE.add(new Coordinate(nextI, nextJ));
                    }
                }
            }
        }
    }

    private static void bfs() {
        while (!CHEESE_QUEUE.isEmpty()) {
            remainCheeses = CHEESE_QUEUE.size();
            hour++;

            Coordinate cheese = null;
            for (int cycle = 0; cycle < remainCheeses; cycle++) {
                cheese = CHEESE_QUEUE.poll();

                box[cheese.i][cheese.j] = 0;
            }

            if (cheese != null) {
                airVisit = new boolean[n][m];
                airVisit[cheese.i][cheese.j] = true;
                AIR_QUEUE.add(new Coordinate(cheese.i, cheese.j));
                getMeltingCheeses();
            }
        }
    }


    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        box = new int[n][m];
        airVisit = new boolean[n][m];
        cheeseVisit = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < m; j++) {
                box[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        airVisit[0][0] = true;
        AIR_QUEUE.add(new Coordinate(0, 0));
        getMeltingCheeses();
        bfs();

        bw.write(hour + "\n");
        bw.write(String.valueOf(remainCheeses));

        bw.flush();
        bw.close();
        br.close();
    }
}