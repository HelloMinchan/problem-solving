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

    private static void union(int a, int b) {
        int findA = find(a);
        int findB = find(b);

        if (findA < findB) {
            disjointSet[findB] = findA;
        } else {
            disjointSet[findA] = findB;
        }
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        disjointSet = new int[n + 1];

        for (int i = 1; i < n + 1; i++) {
            disjointSet[i] = i;
        }

        while (m-- != 0) {
            st = new StringTokenizer(br.readLine());

            int oper = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (oper == 0) {
                union(a, b);
            } else {
                if (find(a) == find(b)) {
                    bw.write("YES\n");
                } else {
                    bw.write("NO\n");
                }
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}