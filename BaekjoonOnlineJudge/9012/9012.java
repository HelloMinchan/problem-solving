import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int testCase = Integer.parseInt(br.readLine());

        while (testCase-- != 0) {
            Stack<Character> stack = new Stack<Character>();
            String inputString = br.readLine();
            boolean isPossible = true;

            for (int index = 0; index < inputString.length(); index++) {
                char target = inputString.charAt(index);

                if (target == '(') {
                    stack.add(target);
                } else {
                    if (stack.empty()) {
                        isPossible = false;
                        break;
                    } else {
                        stack.pop();
                    }
                }
            }

            if (isPossible && stack.empty()) {
                bw.write("YES" + "\n");
            } else {
                bw.write("NO" + "\n");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}