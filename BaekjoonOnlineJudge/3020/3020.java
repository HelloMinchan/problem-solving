import java.io.*;
import java.util.*;

class Main {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static StringTokenizer st;
	private static int n, h;
	private static int[] bottom;
	private static int[] top;
	
	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int h = Integer.parseInt(st.nextToken());
		
		bottom =  new int[h+1];
		top = new int[h+1];
		
		boolean isRockSeed = true;
		for (int i = 0; i < n; i++) {
			if (isRockSeed) {
				bottom[Integer.parseInt(br.readLine())]++;
			} else {
				top[Integer.parseInt(br.readLine())]++;
			}
			isRockSeed = !isRockSeed;
		}
		
		int answerValue = n;
		int answerCount = 0;
		
		int[] bottomSum = new int[h + 1];
		int[] topSum = new int[h + 1];
		
		for (int i = 1; i < h + 1; i++) {
			bottomSum[i] = bottomSum[i - 1] + bottom[i];
			topSum[i] = topSum[i - 1] + top[i];
		}
		
		for (int i = 1; i < h + 1; i++) {
			int crushCount = 0;
			
			crushCount += bottomSum[h] - bottomSum[i - 1];
			crushCount += topSum[h] - topSum[h - i];
			
			if (answerValue > crushCount) {
				answerValue = crushCount;
				answerCount = 1;
			} else if (answerValue == crushCount) {
				answerCount++;
			}
		}
		
		System.out.println(answerValue + " " + answerCount);
	}
}