import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        int totalPrice = Integer.parseInt(br.readLine());
        int kindCount = Integer.parseInt(br.readLine());
        int answer = 0;

        while (kindCount-- != 0) {
            st = new StringTokenizer(br.readLine());

            int price = Integer.parseInt(st.nextToken());
            int count = Integer.parseInt(st.nextToken());

            answer += price * count;
        }

        if (totalPrice == answer) {
            bw.write("Yes");
        } else {
            bw.write("No");
        }
        
        bw.flush();
        bw.close();
        br.close();
    }
}