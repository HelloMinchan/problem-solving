import java.io.*;
import java.util.*;


public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;

    private static Map<String, String> disjointSet;
    private static Map<String, Integer> networkCount;

    private static String find(String target) {
        if (disjointSet.get(target) == target) {
            return target;
        }

        disjointSet.put(target, find(disjointSet.get(target)));
        return disjointSet.get(target);
    }

    private static void union(String f1, String f2) {
        String findF1 = find(f1);
        String findF2 = find(f2);

        if (findF1.equals(findF2)) {
            return;
        }

        if (findF1.compareTo(f2) < 0) {
            disjointSet.put(findF2, findF1);
            networkCount.put(findF1, networkCount.get(findF1) + networkCount.get(findF2));

        } else {
            disjointSet.put(findF1, findF2);
            networkCount.put(findF2, networkCount.get(findF2) + networkCount.get(findF1));
        }
    }

    public static void main(String[] args) throws IOException {
        int testCase = Integer.parseInt(br.readLine());

        while (testCase-- != 0) {
            disjointSet = new HashMap<>();
            networkCount = new HashMap<>();
            int f = Integer.parseInt(br.readLine());

            while (f-- != 0) {
                st = new StringTokenizer(br.readLine());

                String f1 = st.nextToken();
                String f2 = st.nextToken();

                if (!disjointSet.containsKey(f1)) {
                    disjointSet.put(f1, f1);
                    networkCount.put(f1, 1);
                }

                if (!disjointSet.containsKey(f2)) {
                    disjointSet.put(f2, f2);
                    networkCount.put(f2, 1);
                }

                union(f1, f2);

                bw.write(networkCount.get(find(f1)) + "\n");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}