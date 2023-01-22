import java.io.*;
import java.util.*;


class Node {

    int vertex;
    int weight;

    Node(int vertex, int weight) {
        this.vertex = vertex;
        this.weight = weight;
    }
}

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static int n, m;
    private static long[] distance;
    private static ArrayList<ArrayList<Node>> adjacentList;
    private static final int INF = Integer.MAX_VALUE;

    private static boolean bellmanFord() {
        boolean isPossible = true;

        for (int repeat = 0; repeat < n; repeat++) {
            for (int i = 1; i < n + 1; i++) {
                for (Node node : adjacentList.get(i)) {
                    if (distance[i] != INF && distance[i] + node.weight < distance[node.vertex]) {
                        distance[node.vertex] = distance[i] + node.weight;

                        if (repeat == n - 1) {
                            isPossible = false;
                        }
                    }
                }
            }
        }

        return isPossible;
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        distance = new long[n + 1];
        adjacentList = new ArrayList<>();
        for (int i = 0; i < n + 1; i++) {
            adjacentList.add(new ArrayList<>());

            distance[i] = INF;
        }
        distance[1] = 0;

        while (m-- != 0) {
            st = new StringTokenizer(br.readLine());

            int startVertex = Integer.parseInt(st.nextToken());
            int endVertex = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            adjacentList.get(startVertex).add(new Node(endVertex, weight));
        }

        if (bellmanFord()) {
            for (int i = 2; i < n + 1; i++) {
                if (distance[i] == INF) {
                    bw.write("-1\n");
                } else {
                    bw.write(distance[i] + "\n");
                }
            }
        } else {
            bw.write("-1");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}