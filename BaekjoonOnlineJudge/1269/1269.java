import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        int setACount = Integer.parseInt(st.nextToken());
        int setBCount = Integer.parseInt(st.nextToken());

        Set<Integer> setA = new HashSet<>();
        Set<Integer> setB = new HashSet<>();

        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            setA.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            setB.add(Integer.parseInt(st.nextToken()));
        }

        Set<Integer> setAMinusB = setA.stream().filter(number -> !setB.contains(number)).collect(
            Collectors.toSet());
        Set<Integer> setBMinusA = setB.stream().filter(number -> !setA.contains(number)).collect(
            Collectors.toSet());

        setAMinusB.addAll(setBMinusA);

        bw.write(String.valueOf(setAMinusB.size()));

        bw.flush();
        bw.close();
        br.close();
    }
}