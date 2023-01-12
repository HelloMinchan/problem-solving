import java.io.*;
import java.util.*;

class Jewel implements Comparable<Jewel> {

    int weight;
    int price;

    public Jewel(int weight, int price) {
        this.weight = weight;
        this.price = price;
    }

    @Override
    public int compareTo(Jewel target) {
        return target.price - this.price;
    }
}

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        ArrayList<Jewel> jewelInfos = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            jewelInfos.add(
                new Jewel(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }
        Collections.sort(jewelInfos, (jewel1, jewel2) -> jewel1.weight - jewel2.weight);

        ArrayList<Integer> bags = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            bags.add(Integer.parseInt(br.readLine()));
        }
        Collections.sort(bags);

        long answer = 0;
        PriorityQueue<Jewel> bestJewel = new PriorityQueue<>();

        int index = 0;
        for (int bag : bags) {
            while (index < jewelInfos.size() && jewelInfos.get(index).weight <= bag) {
                bestJewel.add(jewelInfos.get(index));
                index++;
            }

            if (!bestJewel.isEmpty()) {
                answer += bestJewel.poll().price;
            }
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}