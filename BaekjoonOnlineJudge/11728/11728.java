import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        String[] arrayA = br.readLine().split(" ");
        String[] arrayB = br.readLine().split(" ");

        int pA = 0;
        int pB = 0;
        ArrayList<Integer> answer = new ArrayList<>();

        while (true) {
            int vA = Integer.parseInt(arrayA[pA]);
            int vB = Integer.parseInt(arrayB[pB]);

            if (vA < vB) {
                answer.add(vA);
                pA++;

                if (pA == n) {
                    break;
                }
            } else {
                answer.add(vB);
                pB++;

                if (pB == m) {
                    break;
                }
            }
        }

        while (pA != n) {
            answer.add(Integer.parseInt(arrayA[pA++]));
        }
        while (pB != m) {
            answer.add(Integer.parseInt(arrayB[pB++]));
        }

        for (int number : answer) {
            bw.write(number + " ");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}