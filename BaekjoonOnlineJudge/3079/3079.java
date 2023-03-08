import java.io.*;
import java.util.*;

class Main {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static StringTokenizer st;
	private static int[] checkTimes;
	
	private static long getCheckedPeopleCountByTime(long time) {
		long peopleCount = 0;
		
		for (int checkTime : checkTimes) {
			peopleCount += time / checkTime;
		}
		
		return peopleCount;
	}
	
	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		
		int checkCount = Integer.parseInt(st.nextToken());
		int friendCount = Integer.parseInt(st.nextToken());
		
		checkTimes = new int[checkCount];
		for (int i = 0; i < checkCount; i++) {
			checkTimes[i] = Integer.parseInt(br.readLine());
		}
		
		long answer = Long.MAX_VALUE;
		long left = 1;
		long right = (long) (Arrays.stream(checkTimes).min().getAsInt() * (long) friendCount);
		
		while (left <= right) {
			long time = (long) ((left + right) / 2);
			
			if (getCheckedPeopleCountByTime(time) >= friendCount) {
				answer = Math.min(answer, time);
				right = time - 1;
			} else {
				left = time + 1;
			}
		}
		
		System.out.println(answer);
	}
}