import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        final int MAX_NUMBER = n + 3;

        boolean[] attCheck = new boolean[MAX_NUMBER];
        int[] notAttCount = new int[MAX_NUMBER];

        st = new StringTokenizer(br.readLine());

        Set<Integer> sleepStudents = new HashSet<>();
        for (int i = 0; i < k; i++) {
            sleepStudents.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < q; i++) {
            int startAttIndex = Integer.parseInt(st.nextToken());
            if (sleepStudents.contains(startAttIndex)) {
                continue;
            }

            int multi = 2;
            int attIndex = startAttIndex;
            while (attIndex < MAX_NUMBER) {
                if (!sleepStudents.contains(attIndex)) {
                    attCheck[attIndex] = true;
                }
                attIndex = startAttIndex * multi++;
            }
        }

        for (int i = 3; i < MAX_NUMBER; i++) {
            if (!attCheck[i]) {
                notAttCount[i] = notAttCount[i - 1] + 1;
            } else {
                notAttCount[i] = notAttCount[i - 1];
            }
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());

            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());

            bw.write(notAttCount[right] - notAttCount[left - 1] + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}