import java.util.Scanner;

public class Solution {
    //숫자 및 "-"로 변환하여 출력하는  함수
    public static void printDash(int num) {
	int dash = 0;	//"-"의 개수
	char temp = ' ';    //각 자리의 숫자를 문자로 임시저장

	for(int i=1;i<=num;i++){
	    String n = Integer.toString(i);
	    for(int j=0;j<n.length();j++) {
		temp = n.charAt(j);
		//3, 6, 9 발견시 "-"의 개수 증가
		if(temp == '3' || temp == '6' || temp == '9')
		    dash++;
	    }
	    //"-"의 개수가 0일시 그냥 숫자 출력
	    if(dash==0)
		System.out.print(i+" ");
	    //"-"의 개수가 0이 아닐시 "-" 출력
	    else {
		for(int j=0;j<dash;j++) {
		    System.out.print("-");
		}
		dash = 0;
		System.out.print(" ");
	    }
	}
    }
    public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	int num = sc.nextInt();

	printDash(num);
    }
}
