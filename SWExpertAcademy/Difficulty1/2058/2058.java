import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);

	int N = sc.nextInt();
	String n = "";
	int sum = 0;

	n = Integer.toString(N);

	for (int i = 0; i < n.length(); i++) {
	    sum += n.charAt(i) - '0';
	}

	System.out.println(sum);
    }
}
