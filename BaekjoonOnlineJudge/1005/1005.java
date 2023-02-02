import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static int n, k, w;
    private static int[] spendingTimes, indegree, techTrees;
    private static ArrayList<ArrayList<Integer>> adjList;
    private static Queue<Integer> queue;

    private static void topologicalSort() {
        for (int node = 1; node < n + 1; node++) {
            if (indegree[node] == 0) {
                queue.add(node);
            }
        }

        while (!queue.isEmpty()) {
            int target = queue.poll();

            for (int node : adjList.get(target)) {
                techTrees[node] = Math.max(techTrees[node],
                    techTrees[target] + spendingTimes[node]);
                indegree[node]--;

                if (indegree[node] == 0) {
                    queue.add(node);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        int testCase = Integer.parseInt(br.readLine());

        while (testCase-- != 0) {
            st = new StringTokenizer(br.readLine());

            n = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());

            adjList = new ArrayList<>();
            for (int i = 0; i < n + 1; i++) {
                adjList.add(new ArrayList<>());
            }

            spendingTimes = new int[n + 1];
            indegree = new int[n + 1];
            techTrees = new int[n + 1];

            st = new StringTokenizer(br.readLine());

            for (int i = 1; i < n + 1; i++) {
                techTrees[i] = spendingTimes[i] = Integer.parseInt(st.nextToken());
            }

            for (int i = 0; i < k; i++) {
                st = new StringTokenizer(br.readLine());

                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());

                adjList.get(x).add(y);
                indegree[y]++;
            }

            w = Integer.parseInt(br.readLine());
            queue = new LinkedList<>();

            topologicalSort();

            bw.write(techTrees[w] + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}