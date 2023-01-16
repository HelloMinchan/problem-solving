import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;
    private static int n, m;
    private static int[] budgets;

    private static int getDistributedBudget(int maxiumBudget) {
        int distributedBudget = 0;

        for (int budget : budgets) {
            if (budget > maxiumBudget) {
                distributedBudget += maxiumBudget;
            } else {
                distributedBudget += budget;
            }
        }

        return distributedBudget;
    }

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        budgets = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            budgets[i] = Integer.parseInt(st.nextToken());
        }
        m = Integer.parseInt(br.readLine());

        int answer = 0;
        int left = 1;
        int right = Arrays.stream(budgets).max().getAsInt();

        while (left <= right) {
            int mid = (left + right) / 2;

            if (getDistributedBudget(mid) > m) {
                right = mid - 1;
            } else {
                answer = Math.max(answer, mid);
                left = mid + 1;
            }
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}