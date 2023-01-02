import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        Set<String> differentStringSet = new HashSet<>();

        String targetString = br.readLine();

        for (int i = 0; i < targetString.length(); i++) {
            StringBuilder tempString = new StringBuilder(String.valueOf(targetString.charAt(i)));
            differentStringSet.add(tempString.toString());
            for (int j = i + 1; j < targetString.length(); j++) {
                tempString.append(targetString.charAt(j));
                differentStringSet.add(tempString.toString());
            }
        }
        
        bw.write(String.valueOf(differentStringSet.size()));

        bw.flush();
        bw.close();
        br.close();
    }
}