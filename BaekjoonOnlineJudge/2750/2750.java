import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> numbers = new ArrayList<Integer>();

        while (n-- != 0) {
            numbers.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(numbers);
        
        for (int number : numbers) {
            bw.write(number + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}