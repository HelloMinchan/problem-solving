import java.io.*;
import java.util.*;

class FinalInputData {

    int maxN;
    int maxM;


    FinalInputData(int maxN, int maxM) {
        this.maxN = maxN;
        this.maxM = maxM;

    }
}

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    static final int MAX_N;
    static final int MAX_M;
    static final int MAX_LENGTH = 51;
    static final int MAX_CHESS_LENGTH = 8;

    static final char[][] BOARD = new char[MAX_LENGTH][MAX_LENGTH];

    private static Optional<FinalInputData> setInput() {
        try {
            st = new StringTokenizer(br.readLine());
            final int maxN = Integer.parseInt(st.nextToken());
            final int maxM = Integer.parseInt(st.nextToken());

            for (int i = 0; i < maxN; i++) {
                String line = br.readLine();

                for (int j = 0; j < maxM; j++) {
                    BOARD[i][j] = line.charAt(j);
                }
            }

            return Optional.of(new FinalInputData(maxN, maxM));
        } catch (IOException e) {
            return Optional.empty();
        }
    }

    static {
        FinalInputData input = setInput().get();

        MAX_N = input.maxN;
        MAX_M = input.maxM;
    }

    private static int getRetouchCount(int startI, int startJ) {
        int whiteStartRetouchCount = 0;
        int blackStartRetouchCount = 0;

        boolean whiteStartFlag = false;
        boolean blackStartFlag = false;

        for (int i = startI; i < startI + MAX_CHESS_LENGTH; i++) {
            for (int j = startJ; j < startJ + MAX_CHESS_LENGTH; j++) {
                whiteStartFlag = !whiteStartFlag;
                blackStartFlag = !blackStartFlag;

                if (whiteStartFlag) {
                    if (BOARD[i][j] != 'W') {
                        whiteStartRetouchCount++;
                    }
                } else {
                    if (BOARD[i][j] != 'B') {
                        whiteStartRetouchCount++;
                    }
                }

                if (blackStartFlag) {
                    if (BOARD[i][j] != 'B') {
                        blackStartRetouchCount++;
                    }
                } else {
                    if (BOARD[i][j] != 'W') {
                        blackStartRetouchCount++;
                    }
                }
            }

            whiteStartFlag = !whiteStartFlag;
            blackStartFlag = !blackStartFlag;
        }
        
        return Math.min(whiteStartRetouchCount, blackStartRetouchCount);
    }


    public static void main(String[] args) throws IOException {
        int answer = Integer.MAX_VALUE;

        for (int i = 0; i < MAX_N - MAX_CHESS_LENGTH + 1; i++) {
            for (int j = 0; j < MAX_M - MAX_CHESS_LENGTH + 1; j++) {
                int retouchCount = getRetouchCount(i, j);

                if (answer >= retouchCount) {
                    answer = retouchCount;
                }
            }
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}