import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());

        while (n-- != 0) {
            Stack<Character> stack = new Stack<>();
            boolean isPossible = true;

            String input = br.readLine();

            for (int i = 0; i < input.length(); i++) {
                char ps = input.charAt(i);

                if (ps == '(') {
                    stack.add(ps);
                } else {
                    if (!stack.empty() && stack.peek() == '(') {
                        stack.pop();
                    } else {
                        isPossible = false;
                        break;
                    }
                }
            }

            if (isPossible && stack.empty()) {
                bw.write("YES\n");
            } else {
                bw.write("NO\n");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}