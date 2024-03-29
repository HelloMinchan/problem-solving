import java.io.*;
import java.util.*;


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] pieces = br.readLine().split(" ");
        int[] chess = {1, 1, 2, 2, 2, 8};
        StringBuilder answer = new StringBuilder();

        for (int i = 0; i < chess.length; i++) {
            answer.append(chess[i] - Integer.parseInt(pieces[i]) + " ");
        }

        bw.write(answer + "\n");

        bw.flush();
        bw.close();
        br.close();
    }
}