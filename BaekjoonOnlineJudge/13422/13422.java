import java.io.*;
import java.util.*;

class Main {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static StringTokenizer st;
	
	public static void main(String[] args) throws Exception {
		int testCase = Integer.parseInt(br.readLine());
		
		while (testCase-- != 0) {
			st = new StringTokenizer(br.readLine());
			
			int houseCount = Integer.parseInt(st.nextToken());
			int minimumThiefCount = Integer.parseInt(st.nextToken());
			int limitAmount = Integer.parseInt(st.nextToken());
			
			int[] houses = new int[houseCount];
			st = new StringTokenizer(br.readLine());
			for (int index = 0; index < houseCount; index++) {
				houses[index] = Integer.parseInt(st.nextToken());
			}
			
			if (houseCount == minimumThiefCount) {
				if (Arrays.stream(houses).sum() < limitAmount) {
					System.out.println(1);
				} else {
					System.out.println(0);
				}
			} else {
				int answer = 0;
				int left = 0;
				int right = 0;
				int window = houses[0];

				while (right < houseCount + minimumThiefCount - 1) {
					if (right - left == minimumThiefCount - 1) {
						if (window < limitAmount) {
							answer++;
						}

						window -= houses[left];
						left++;
						right++;
						if (right < houseCount + minimumThiefCount - 1) {
							window += houses[right % houseCount];	
						}
					} else {
						right++;
						if (right < houseCount + minimumThiefCount - 1) {
							window += houses[right % houseCount];
						}
					}
				}

				System.out.println(answer);
			}
		}
	}
}