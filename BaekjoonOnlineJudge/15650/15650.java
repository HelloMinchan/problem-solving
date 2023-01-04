import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static final int MAX_NUMBER = 9;
    private static boolean[] visit = new boolean[MAX_NUMBER];
    private static Stack<Integer> stack = new Stack<>();

    private static void dfs(int n, int m, int depth) {
        if (stack.size() == m) {
            StringBuilder sb = new StringBuilder();

            stack.stream().forEach((number) -> {
                sb.append(number + " ");
            });

            System.out.println(sb.toString());

            return;
        }

        for (int number = depth; number <= n; number++) {
            if (!visit[number]) {
                visit[number] = true;
                stack.add(number);
                dfs(n, m, number);
                visit[number] = false;
                stack.pop();
            }
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