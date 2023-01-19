import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static int[] disjointSet;

    private static int find(int target) {
        if (disjointSet[target] == target) {
            return target;
        }

        disjointSet[target] = find(disjointSet[target]);
        return disjointSet[target];
    }

    private static void union(int city1, int city2) {
        int findCity1 = find(city1);
        int findCity2 = find(city2);

        if (findCity1 < findCity2) {
            disjointSet[findCity2] = findCity1;
        } else {
            disjointSet[findCity1] = findCity2;
        }
    }

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        disjointSet = new int[n + 1];
        for (int city = 1; city < n + 1; city++) {
            disjointSet[city] = city;
        }

        for (int i = 1; i < n + 1; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 1; j < n + 1; j++) {
                int isConnect = Integer.parseInt(st.nextToken());

                if (isConnect == 1) {
                    union(i, j);
                }
            }
        }

        String[] plan = br.readLine().split(" ");

        boolean isPossible = true;
        int connectCity = find(Integer.parseInt(plan[0]));
        for (int city = 1; city < m; city++) {
            if (find(connectCity) != find(Integer.parseInt(plan[city]))) {
                isPossible = false;
                break;
            }
        }

        if (isPossible) {
            bw.write("YES");
        } else {
            bw.write("NO");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}