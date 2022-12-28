import java.io.*;
import java.util.*;
import java.util.stream.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static final int MAX_LENGTH = 9;


    public static void main(String[] args) throws IOException {
        int[][] matrix = new int[MAX_LENGTH][MAX_LENGTH];

        for (int i = 0; i < MAX_LENGTH; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < MAX_LENGTH; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int maxNumber = 0;
        int maxNumberI = 0;
        int maxNumberJ = 0;

        for (int i = 0; i < MAX_LENGTH; i++) {
            for (int j = 0; j < MAX_LENGTH; j++) {
                if (maxNumber <= matrix[i][j]) {
                    maxNumber = matrix[i][j];
                    maxNumberI = i;
                    maxNumberJ = j;
                }
            }
        }

        bw.write(maxNumber + "\n");
        bw.write(++maxNumberI + " " + ++maxNumberJ);

        bw.flush();
        bw.close();
        br.close();
    }
}