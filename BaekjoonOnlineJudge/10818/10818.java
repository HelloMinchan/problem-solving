import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int count = Integer.parseInt(br.readLine());
        ArrayList<Integer> numbers = new ArrayList<Integer>();

        st = new StringTokenizer(br.readLine());

        for (int index = 0; index < count; index++) {
            numbers.add(Integer.parseInt(st.nextToken()));
        }

        bw.write(Collections.min(numbers) + " " + Collections.max(numbers));

        bw.flush();
        bw.close();
        br.close();
    }
}