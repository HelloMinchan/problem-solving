import java.io.*;
import java.util.*;

class Pair {

    int i;
    int j;

    Pair(int i, int j) {
        this.i = i;
        this.j = j;
    }
}

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static final int MAX_LENGTH = 10;
    public static int[][] sudoku = new int[MAX_LENGTH][MAX_LENGTH];

    private static ArrayList<Pair> zeroList = new ArrayList<>();
    private static Pair[] zeroArray;
    private static boolean[][] rowVisit = new boolean[MAX_LENGTH][MAX_LENGTH];
    private static boolean[][] colVisit = new boolean[MAX_LENGTH][MAX_LENGTH];

    private static boolean checkDistrict(int number, int zeroI, int zeroJ) {
        int iDistrict = (zeroI - 1) / 3;
        int jDistrict = (zeroJ - 1) / 3;

        for (int i = iDistrict * 3 + 1; i < iDistrict * 3 + 4; i++) {
            for (int j = jDistrict * 3 + 1; j < jDistrict * 3 + 4; j++) {
                if (sudoku[i][j] == number) {
                    return false;
                }
            }
        }

        return true;
    }

    private static void solveSudoku(int solveIndex) {
        if (solveIndex >= zeroArray.length) {
            for (int i = 1; i < MAX_LENGTH; i++) {
                StringBuilder sb = new StringBuilder();

                for (int j = 1; j < MAX_LENGTH; j++) {
                    sb.append(sudoku[i][j] + " ");
                }

                System.out.println(sb.toString());
            }

            System.exit(0);
        }

        Pair zero = zeroArray[solveIndex];

        for (int number = 1; number < MAX_LENGTH; number++) {
            if (checkDistrict(number, zero.i, zero.j) && !rowVisit[zero.i][number]
                && !colVisit[zero.j][number]) {
                sudoku[zero.i][zero.j] = number;
                rowVisit[zero.i][number] = true;
                colVisit[zero.j][number] = true;
                solveSudoku(solveIndex + 1);
                sudoku[zero.i][zero.j] = 0;
                rowVisit[zero.i][number] = false;
                colVisit[zero.j][number] = false;
            }
        }

    }

    public static void main(String[] args) throws IOException {
        for (int i = 1; i < MAX_LENGTH; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 1; j < MAX_LENGTH; j++) {
                sudoku[i][j] = Integer.parseInt(st.nextToken());
                rowVisit[i][sudoku[i][j]] = true;
                colVisit[j][sudoku[i][j]] = true;

                if (sudoku[i][j] == 0) {
                    zeroList.add(new Pair(i, j));
                }
            }
        }

        zeroArray = zeroList.stream().toArray(Pair[]::new);

        solveSudoku(0);

        bw.flush();
        bw.close();
        br.close();
    }
}