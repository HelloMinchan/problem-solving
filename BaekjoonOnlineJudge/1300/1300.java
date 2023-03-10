import java.io.*;
class Main {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main(String[] args) throws Exception {
		int N = Integer.parseInt(br.readLine());
		int K = Integer.parseInt(br.readLine());
		
		long left = 1;
		long right = K;
		
		while (left <= right) {
			long mid = (left + right) / 2;
			
			long count = 0;
			
			for (int i = 1; i <= N; i++) {
				count += Math.min(mid / i, N);
			}
			
			if (K <= count) {
				right = mid - 1;
			} else {
				left = mid + 1;
			}
		}
		
		System.out.println(left);
	}
}