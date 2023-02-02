import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static int n, m;
    private static int[] indegree;
    private static ArrayList<ArrayList<Integer>> adjacentList = new ArrayList<>();
    private static Queue<Integer> queue = new LinkedList<>();
    private static StringBuilder sb = new StringBuilder();

    private static void topologicalSort() {
        for (int i = 1; i < n + 1; i++) {
            if (indegree[i] == 0) {
                queue.add(i);
            }
        }

        while (!queue.isEmpty()) {
            int target = queue.poll();
            sb.append(target + " ");

            for (int node : adjacentList.get(target)) {
                indegree[node]--;

                if (indegree[node] == 0) {
                    queue.add(node);
                }
            }
        }
    }


    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        indegree = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            adjacentList.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            adjacentList.get(a).add(b);
            indegree[b]++;
        }

        topologicalSort();

        bw.write(sb.toString());

        bw.flush();
        bw.close();
        br.close();
    }
}