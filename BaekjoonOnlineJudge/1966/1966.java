import java.io.*;
import java.util.*;

class Document {

    int sequence;
    int priority;

    Document(int sequence, int priority) {
        this.sequence = sequence;
        this.priority = priority;
    }
}

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int testCase = Integer.parseInt(br.readLine());

        while (testCase-- != 0) {
            st = new StringTokenizer(br.readLine());

            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());

            Queue<Document> printer = new LinkedList<>();
            PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

            for (int sequence = 0; sequence < n; sequence++) {
                int priority = Integer.parseInt(st.nextToken());

                pq.add(priority);
                printer.add(new Document(sequence, priority));
            }

            int answer = 0;
            int priority = n;
            while (true) {
                Document document = printer.poll();

                if (document.priority == pq.peek()) {
                    answer++;
                    pq.remove();

                    if (document.sequence == m) {
                        break;
                    }
                } else {
                    printer.add(document);
                }
            }

            bw.write(answer + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}