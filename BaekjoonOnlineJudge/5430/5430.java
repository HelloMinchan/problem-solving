import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int testCase = Integer.parseInt(br.readLine());

        while (testCase-- != 0) {
            String functions = br.readLine();
            int n = Integer.parseInt(br.readLine());
            String numbers = br.readLine();

            numbers = numbers.substring(1, numbers.length() - 1);
            String[] numbersArray = numbers.split(",");
            Deque<String> numberQueue = new LinkedList<>();

            if (!numbers.equals("")) {
                for (String number : numbersArray) {
                    numberQueue.add(number);
                }
            }

            boolean isReverse = false;
            boolean isError = false;
            for (int i = 0; i < functions.length(); i++) {
                if (functions.charAt(i) == 'R') {
                    isReverse = !isReverse;
                } else {
                    if (numberQueue.isEmpty()) {
                        isError = true;
                    } else {
                        if (isReverse) {
                            numberQueue.removeLast();
                        } else {
                            numberQueue.remove();
                        }
                    }
                }
            }

            if (isError) {
                bw.write("error\n");
            } else {
                StringBuilder sb = new StringBuilder("[");

                while (!numberQueue.isEmpty()) {
                    String number;
                    if (isReverse) {
                        number = numberQueue.pollLast();
                    } else {
                        number = numberQueue.poll();
                    }

                    sb.append(number + ",");
                }

                if (sb.length() != 1) {
                    sb.deleteCharAt(sb.length() - 1);
                }

                sb.append("]");

                bw.write(sb + "\n");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}