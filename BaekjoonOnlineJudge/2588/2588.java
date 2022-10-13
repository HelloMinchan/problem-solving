import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));

        int firstNumber = Integer.parseInt(br.readLine());
        String secondNumber = br.readLine();

        for (int digit = 2; digit >= 0; digit--) {
            System.out.println(firstNumber * Character.getNumericValue(secondNumber.charAt(digit)));
        }
        System.out.println(firstNumber * Integer.parseInt(secondNumber));
    }
}
