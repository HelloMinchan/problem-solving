import java.io.*;
import java.util.*;

class Planet {

    int x;
    int y;
    int z;
    int number;

    public Planet(int x, int y, int z, int number) {
        this.x = x;
        this.y = y;
        this.z = z;
        this.number = number;
    }
}

class Tunnel {

    int weight;
    int from;
    int to;

    public Tunnel(int weight, int from, int to) {
        this.weight = weight;
        this.from = from;
        this.to = to;
    }
}

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static int n, m;
    private static int[] disjointSet;
    private static Planet[] planets;
    private static PriorityQueue<Tunnel> tunnelPq = new PriorityQueue<>(
        (t1, t2) -> t1.weight - t2.weight);
    private static int answer = 0;

    private static int find(int target) {
        if (disjointSet[target] == target) {
            return target;
        }

        return disjointSet[target] = find(disjointSet[target]);
    }

    private static boolean union(int e1, int e2) {
        int findE1 = find(e1);
        int findE2 = find(e2);

        if (findE1 == findE2) {
            return false;
        }

        if (findE1 < findE2) {
            disjointSet[findE2] = findE1;
        } else {
            disjointSet[findE1] = findE2;
        }

        return true;
    }

    private static void kruskal() {
        int tunnelCount = 0;

        while (!tunnelPq.isEmpty()) {
            Tunnel t = tunnelPq.poll();

            if (union(t.from, t.to)) {
                answer += t.weight;
                tunnelCount++;

                if (tunnelCount == n - 1) {
                    return;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());

        disjointSet = new int[n];
        planets = new Planet[n];

        for (int i = 0; i < n; i++) {
            disjointSet[i] = i;
        }

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());

            planets[i] = new Planet(x, y, z, i);
        }

        Arrays.sort(planets, (p1, p2) -> p1.x - p2.x);
        for (int i = 0; i < n - 1; i++) {
            tunnelPq.add(new Tunnel(Math.abs(planets[i].x - planets[i + 1].x), planets[i].number,
                planets[i + 1].number));
        }
        Arrays.sort(planets, (p1, p2) -> p1.y - p2.y);
        for (int i = 0; i < n - 1; i++) {
            tunnelPq.add(new Tunnel(Math.abs(planets[i].y - planets[i + 1].y), planets[i].number,
                planets[i + 1].number));
        }
        Arrays.sort(planets, (p1, p2) -> p1.z - p2.z);
        for (int i = 0; i < n - 1; i++) {
            tunnelPq.add(new Tunnel(Math.abs(planets[i].z - planets[i + 1].z), planets[i].number,
                planets[i + 1].number));
        }

        kruskal();

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}