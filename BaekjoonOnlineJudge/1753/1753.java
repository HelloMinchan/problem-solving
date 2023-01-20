import java.io.*;
import java.util.*;

class VertexInfo {

    int vertex;
    int weight;

    public VertexInfo(int vertex, int weight) {
        this.vertex = vertex;
        this.weight = weight;
    }
}


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static int INF = Integer.MAX_VALUE;
    private static int[] dist;
    private static int v, e, k;
    private static ArrayList<ArrayList<VertexInfo>> adjacentList;

    private static void dijkstra() {
        PriorityQueue<VertexInfo> pq = new PriorityQueue<>(
            (vertex1, vertex2) -> vertex1.weight - vertex2.weight);

        for (VertexInfo v : adjacentList.get(k)) {
            pq.add(v);
        }

        while (!pq.isEmpty()) {
            VertexInfo v = pq.poll();

            if (v.weight <= dist[v.vertex]) {
                dist[v.vertex] = v.weight;

                for (VertexInfo newVertex : adjacentList.get(v.vertex)) {
                    if (newVertex.weight + v.weight <= dist[newVertex.vertex]) {
                        pq.add(new VertexInfo(newVertex.vertex, newVertex.weight + v.weight));
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());

        k = Integer.parseInt(br.readLine());

        dist = new int[v + 1];
        for (int i = 0; i < v + 1; i++) {
            dist[i] = INF;
        }
        dist[k] = 0;

        adjacentList = new ArrayList<>();
        for (int i = 0; i < v + 1; i++) {
            adjacentList.add(new ArrayList<>());
        }

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());

            int startVertex = Integer.parseInt(st.nextToken());
            int endVertex = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            adjacentList.get(startVertex).add(new VertexInfo(endVertex, weight));
        }

        dijkstra();

        for (int i = 1; i < v + 1; i++) {
            if (dist[i] == INF) {
                bw.write("INF\n");
            } else {
                bw.write(dist[i] + "\n");
            }

        }

        bw.flush();
        bw.close();
        br.close();
    }
}