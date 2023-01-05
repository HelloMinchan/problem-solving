import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        Set<Integer> numbers = new HashSet<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            numbers.add(Integer.parseInt(st.nextToken()));
        }

        numbers.stream().sorted().forEach(number -> {
            System.out.print(number + " ");

        });

        bw.flush();
        bw.close();
        br.close();
    }
}