import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static final int maxCount = 28;
    private static final int maxNumber = 30;


    public static void main(String[] args) throws IOException {
        ArrayList<Integer> numbers = new ArrayList<Integer>();

        for (int i = 0; i < maxCount; i++) {
            numbers.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(numbers);

        for (int number = 1; number <= maxNumber; number++) {
            if (numbers.indexOf(number) == -1) {
                bw.write(number + "\n");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}