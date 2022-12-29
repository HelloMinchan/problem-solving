import java.io.*;
import java.util.*;
import java.util.stream.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    private static void fibonacci(final int MAX_DEPTH, int depth, int number1, int number2)
        throws IOException {
        if (MAX_DEPTH == depth) {
            bw.write(String.valueOf(number1 + number2));
        } else {
            fibonacci(MAX_DEPTH, depth + 1, number2, number1 + number2);
        }
    }


    public static void main(String[] args) throws IOException {
        final int MAX_DEPTH = Integer.parseInt(br.readLine());

        switch (MAX_DEPTH) {
            case 0:
                bw.write("0");
                break;
            case 1:
            case 2:
                bw.write("1");
                break;
            default:
                fibonacci(MAX_DEPTH, 3, 1, 1);
        }

        bw.flush();
        bw.close();
        br.close();
    }
}