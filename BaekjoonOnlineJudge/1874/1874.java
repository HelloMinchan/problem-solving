import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        Queue<Integer> sequence = new LinkedList<>();
        Stack<Integer> stack = new Stack<>();
        ArrayList<String> answer = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            sequence.add(Integer.parseInt(br.readLine()));
        }

        int number = 1;
        while (number <= n) {
            while (number <= n && number != sequence.peek()) {
                stack.add(number++);
                answer.add("+");
            }

            if (number > n) {
                break;
            } else {
                stack.add(number++);
                answer.add("+");
            }

            while (!stack.empty() && !sequence.isEmpty() && stack.peek().equals(sequence.peek())) {
                stack.pop();
                sequence.remove();
                answer.add("-");
            }
        }

        if (sequence.size() == 0) {
            answer.stream().forEach(System.out::println);
        } else {
            System.out.println("NO");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}