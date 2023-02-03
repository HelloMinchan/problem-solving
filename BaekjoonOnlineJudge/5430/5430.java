import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int testCase = Integer.parseInt(br.readLine());

        while (testCase-- != 0) {
            char[] opers = br.readLine().toCharArray();
            int n = Integer.parseInt(br.readLine());

            String preArray = br.readLine();
            preArray = preArray.substring(1, preArray.length() - 1);

            String[] array;
            if (preArray.equals("")) {
                array = new String[0];
            } else {
                array = preArray.split(",");
            }

            Deque<String> dequeue = new LinkedList<>();
            for (String number : array) {
                dequeue.add(number);
            }

            boolean isReverse = false;
            boolean isError = false;
            for (char oper : opers) {
                if (oper == 'D') {
                    if (!dequeue.isEmpty()) {
                        if (isReverse) {
                            dequeue.removeLast();
                        } else {
                            dequeue.remove();
                        }
                    } else {
                        isError = true;
                        break;
                    }
                } else {
                    isReverse = !isReverse;
                }
            }

            if (isError) {
                bw.write("error\n");
            } else {
                StringBuilder sb = new StringBuilder("[");

                while (!dequeue.isEmpty()) {
                    if (isReverse) {
                        sb.append(dequeue.pollLast() + ",");
                    } else {
                        sb.append(dequeue.poll() + ",");
                    }

                }

                if (sb.length() > 1) {
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