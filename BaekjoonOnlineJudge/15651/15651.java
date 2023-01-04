import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static final int MAX_NUMBER = 7;
    private static boolean[] visit = new boolean[MAX_NUMBER];
    private static Stack<Integer> stack = new Stack<>();

    private static void dfs(int n, int m, int depth) throws IOException {
        if (stack.size() == m) {
            StringBuilder sb = new StringBuilder();

            stack.stream().forEach((number) -> {
                sb.append(number + " ");
            });

            bw.write(sb.toString() + "\n");

            return;
        }

        for (int number = 1; number <= n; number++) {
            stack.add(number);
            dfs(n, m, number);
            stack.pop();
        }
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        dfs(n, m, 1);

        bw.flush();
        bw.close();
        br.close();
    }
}