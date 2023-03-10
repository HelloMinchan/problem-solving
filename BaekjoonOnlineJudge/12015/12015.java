import java.io.*;
import java.util.*;

class Main {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static StringTokenizer st;
	private static ArrayList<Integer> incrementSequence;
	
	public static int lowerBound(int target) {
		int left = 0;
		int right = incrementSequence.size() - 1;
		
		while (left <= right) {
			int mid = (left + right) / 2;
			
			if (target <= incrementSequence.get(mid)) {
				right = mid - 1;
			} else {
				left = mid + 1;
			}
		}
		
		return left;
	}
	
	public static void main(String[] args) throws Exception {
		int n = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine());
		
		incrementSequence = new ArrayList<>();
		
		while (st.hasMoreTokens()) {
			int target = Integer.parseInt(st.nextToken());
			
			if (incrementSequence.size() == 0 || target > incrementSequence.get(incrementSequence.size() - 1)) {
				incrementSequence.add(target);
			} else {
				int index = lowerBound(target);
				
				incrementSequence.set(index, target);
			}
		}
		
		System.out.println(incrementSequence.size());
	}
}