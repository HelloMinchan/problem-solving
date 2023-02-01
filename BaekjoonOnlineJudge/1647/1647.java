import java.io.*;
import java.util.*;

class Edge {

    int weight;
    int from;
    int to;

    public Edge(int weight, int from, int to) {
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
    private static PriorityQueue<Edge> edgePq = new PriorityQueue<>(
        (e1, e2) -> e1.weight - e2.weight);
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
        int maxWeight = 0;

        while (!edgePq.isEmpty()) {
            Edge e = edgePq.poll();

            if (union(e.from, e.to)) {
                if (maxWeight < e.weight) {
                    maxWeight = e.weight;
                }

                answer += e.weight;
            }
        }

        answer -= maxWeight;
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        disjointSet = new int[n + 1];

        for (int i = 1; i < n + 1; i++) {
            disjointSet[i] = i;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            edgePq.add(new Edge(weight, from, to));
        }

        kruskal();

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}