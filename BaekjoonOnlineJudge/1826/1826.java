import java.io.*;
import java.util.*;

class GasStation implements Comparable<GasStation> {

    int distance;
    int amount;

    public GasStation(int distance, int amount) {
        this.distance = distance;
        this.amount = amount;
    }

    @Override
    public int compareTo(GasStation gs) {
        return this.distance - gs.distance;
    }
}

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int answer = 0;
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<GasStation> targetGasStation = new PriorityQueue<>();
        PriorityQueue<Integer> visitGasStation = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            int distance = Integer.parseInt(st.nextToken());
            int amount = Integer.parseInt(st.nextToken());

            targetGasStation.add(new GasStation(distance, amount));
        }

        st = new StringTokenizer(br.readLine());
        int destination = Integer.parseInt(st.nextToken());
        int remainAmount = Integer.parseInt(st.nextToken());

        while (remainAmount < destination) {
            while (!targetGasStation.isEmpty()
                && targetGasStation.peek().distance <= remainAmount) {
                visitGasStation.add(targetGasStation.poll().amount);
            }

            if (visitGasStation.isEmpty()) {
                answer = -1;
                break;
            } else {
                answer++;
                remainAmount += visitGasStation.poll();
            }
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}