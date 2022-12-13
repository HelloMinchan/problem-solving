import java.io.*;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;


    public static void main(String[] args) throws IOException {
        String number = br.readLine();
        int originalNumber = Integer.parseInt(number);
        String tempNumber = "";
        String sumNumber = "";
        int answer = 0;

        while (true) {
            answer++;

            if (Integer.parseInt(number) < 10) {
                tempNumber = number + "0";
            } else {
                tempNumber = number;
            }

            sumNumber = String.valueOf(
                Character.getNumericValue(tempNumber.charAt(0)) + Character.getNumericValue(
                    tempNumber.charAt(1)));

            String newNumber =
                number.charAt(number.length() - 1) + "" + sumNumber.charAt(sumNumber.length() - 1);

            if (Integer.parseInt(newNumber) == originalNumber) {
                break;
            } else {
                number = newNumber;
            }
        }

        bw.write(String.valueOf(answer));

        bw.flush();
        bw.close();
        br.close();
    }
}