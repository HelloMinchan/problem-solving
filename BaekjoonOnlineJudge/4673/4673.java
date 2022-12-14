import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        Set<Integer> conNumbers = new HashSet<Integer>();
        int number = 1;

        while (number <= 10000) {
            int conNumber = number;
            String strNumber = String.valueOf(number);

            for (int i = 0; i < strNumber.length(); i++) {
                conNumber += Character.getNumericValue(strNumber.charAt(i));
            }

            conNumbers.add(conNumber);

            number++;
        }

        for (int selfNumber = 1; selfNumber <= 10000; selfNumber++) {
            if (!conNumbers.contains(selfNumber)) {
                bw.write(selfNumber + "\n");
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}