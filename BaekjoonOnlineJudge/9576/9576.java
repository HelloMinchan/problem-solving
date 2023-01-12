import java.io.*;
import java.util.*;

class Applicant {

    int start;
    int end;

    public Applicant(int start, int end) {
        this.start = start;
        this.end = end;
    }
}

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int testCase = Integer.parseInt(br.readLine());

        while (testCase-- != 0) {
            int answer = 0;
            st = new StringTokenizer(br.readLine());

            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            boolean[] books = new boolean[n + 1];
            ArrayList<Applicant> applicants = new ArrayList<>();

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());

                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                applicants.add(new Applicant(a, b));
            }

            Collections.sort(applicants, (a1, a2) -> a1.end - a2.end);

            for (Applicant applicant : applicants) {
                for (int index = applicant.start; index <= applicant.end; index++) {
                    if (!books[index]) {
                        books[index] = true;
                        answer++;
                        break;
                    }
                }
            }

            bw.write(answer + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}