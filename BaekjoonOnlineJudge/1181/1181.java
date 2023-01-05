import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        Set<String> wordSet = new HashSet<>();

        while (n-- != 0) {
            wordSet.add(br.readLine());
        }

        wordSet.stream()
            .sorted(Comparator.comparing(String::length).thenComparing(String::toString))
            .forEach(System.out::println);

        bw.flush();
        bw.close();
        br.close();
    }
}