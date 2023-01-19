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

    private static void union(int gate1, int gate2) {
        int findGate1 = find(gate1);
        int findGate2 = find(gate2);

        if (findGate1 < findGate2) {
            disjointSet[findGate2] = findGate1;
        } else {
            disjointSet[findGate1] = findGate2;
        }
    }

    public static void main(String[] args) throws IOException {
        int g = Integer.parseInt(br.readLine());
        disjointSet = new int[g + 1];
        for (int gate = 1; gate < g + 1; gate++) {
            disjointSet[gate] = gate;
        }

        int p = Integer.parseInt(br.readLine());

        int answer = 0;
        while (p-- != 0) {
            int destination = find(Integer.parseInt(br.readLine()));

            if (destination == 0) {
                break;
            } else {
                answer++;
                union(destination, destination - 1);
            }
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}