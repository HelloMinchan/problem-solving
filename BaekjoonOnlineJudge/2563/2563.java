import java.io.*;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static final int WHITE_PAPER_SIZE = 101;
    private static final int COLOR_PAPER_SIZE = 10;

    public static void main(String[] args) throws IOException {
        int[][] whitePaper = new int[WHITE_PAPER_SIZE][WHITE_PAPER_SIZE];
        int answer = 0;

        int colorPaperCount = Integer.parseInt(br.readLine());

        while (colorPaperCount-- != 0) {
            st = new StringTokenizer(br.readLine());

            int startJ = Integer.parseInt(st.nextToken());
            int startI = Integer.parseInt(st.nextToken());

            for (int i = WHITE_PAPER_SIZE - startI;
                i > WHITE_PAPER_SIZE - startI - COLOR_PAPER_SIZE; i--) {
                for (int j = startJ; j < startJ + COLOR_PAPER_SIZE; j++) {
                    whitePaper[i][j] = 1;
                }
            }
        }

        bw.write(String.valueOf(Arrays.stream(whitePaper)
            .mapToInt(row -> (int) Arrays.stream(row).filter(dot -> dot == 1).count()).sum()));

        bw.flush();
        bw.close();
        br.close();
    }
}