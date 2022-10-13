import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));

        int[] chess = {1, 1, 2, 2, 2, 8};
        String[] pieces = br.readLine().split(" ");

        for (int kind = 0; kind < chess.length; kind++) {
            System.out.printf("%d ", chess[kind] - Integer.parseInt(pieces[kind]));
        }
    }
}
