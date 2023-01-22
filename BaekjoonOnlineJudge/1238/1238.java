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

    private static int n, m, x;
    private static ArrayList<ArrayList<Node>> departureAdjacentList;
    private static ArrayList<ArrayList<Node>> arrivalAdjacentList;
    private static int[] depatureDistance;
    private static int[] arrivalDistance;
    private static final int INF = Integer.MAX_VALUE;

    private static void dijkstra() {
        PriorityQueue<Node> pq = new PriorityQueue<>((n1, n2) -> n1.weight - n2.weight);
        for (Node node : departureAdjacentList.get(x)) {
            pq.add(node);
        }

        while (!pq.isEmpty()) {
            Node node = pq.poll();

            if (node.weight <= depatureDistance[node.vertex]) {
                depatureDistance[node.vertex] = node.weight;

                for (Node nextNode : departureAdjacentList.get(node.vertex)) {
                    if (depatureDistance[node.vertex] + nextNode.weight
                        <= depatureDistance[nextNode.vertex]) {
                        pq.add(new Node(nextNode.vertex,
                            depatureDistance[node.vertex] + nextNode.weight));
                    }
                }
            }
        }

        pq = new PriorityQueue<>((n1, n2) -> n1.weight - n2.weight);
        for (Node node : arrivalAdjacentList.get(x)) {
            pq.add(node);
        }

        while (!pq.isEmpty()) {
            Node node = pq.poll();

            if (node.weight <= arrivalDistance[node.vertex]) {
                arrivalDistance[node.vertex] = node.weight;

                for (Node nextNode : arrivalAdjacentList.get(node.vertex)) {
                    if (arrivalDistance[node.vertex] + nextNode.weight
                        <= arrivalDistance[nextNode.vertex]) {
                        pq.add(new Node(nextNode.vertex,
                            arrivalDistance[node.vertex] + nextNode.weight));
                    }
                }
            }
        }
    }


    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());

        departureAdjacentList = new ArrayList<>();
        arrivalAdjacentList = new ArrayList<>();
        for (int i = 0; i < n + 1; i++) {
            departureAdjacentList.add(new ArrayList<>());
            arrivalAdjacentList.add(new ArrayList<>());
        }

        depatureDistance = new int[n + 1];
        arrivalDistance = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            depatureDistance[i] = INF;
            arrivalDistance[i] = INF;
        }
        depatureDistance[x] = 0;
        arrivalDistance[x] = 0;

        while (m-- != 0) {
            st = new StringTokenizer(br.readLine());

            int startVertex = Integer.parseInt(st.nextToken());
            int endVertex = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            departureAdjacentList.get(endVertex).add(new Node(startVertex, weight));
            arrivalAdjacentList.get(startVertex).add(new Node(endVertex, weight));
        }

        dijkstra();

        int answer = 0;
        for (int i = 1; i < n + 1; i++) {
            answer = Math.max(depatureDistance[i] + arrivalDistance[i], answer);
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}