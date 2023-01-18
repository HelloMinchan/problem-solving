import java.io.*;
import java.util.*;

class Movement {

    int from;
    int to;

    public Movement(int from, int to) {
        this.from = from;
        this.to = to;
    }
}

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static ArrayList<Movement> movements = new ArrayList<>();

    private static void solveHanoi(int n, int from, int mid, int to) {
        if (n == 1) {
            movements.add(new Movement(from, to));
            return;
        }

        solveHanoi(n - 1, from, to, mid);
        movements.add(new Movement(from, to));
        solveHanoi(n - 1, mid, from, to);
    }


    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());

        solveHanoi(n, 1, 2, 3);

        bw.write((int) Math.pow(2, n) - 1 + "\n");
        for (Movement movement : movements) {
            bw.write(movement.from + " " + movement.to + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}