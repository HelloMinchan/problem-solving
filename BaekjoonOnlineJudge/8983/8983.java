import java.io.*;
import java.util.*;

class Location {
	int x;
	int y;
	
	Location(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

class Main {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static StringTokenizer st;
	private static int sandBoxCount, animalCount, catchLength;
	private static int[] sandBoxLocation;
	private static Location[] animalLocation;
	
	private static boolean isCatch(int animal) {
		int left = 0;
		int right = sandBoxCount;
		
		while (left <= right) {
			int sandBox = (int) ((left + right) / 2);
			
			if (sandBox >= sandBoxCount) {
				return false;
			}
			
			int animalDistance = Math.abs(sandBoxLocation[sandBox] - animalLocation[animal].x) + animalLocation[animal].y;
			
			if ((catchLength < animalDistance) && animalLocation[animal].x < sandBoxLocation[sandBox]) {
				right = sandBox - 1;
			} else if ((catchLength < animalDistance) && animalLocation[animal].x >= sandBoxLocation[sandBox]) {
				left = sandBox + 1;
			} else if (catchLength >= animalDistance) {
				return true;
			}
		}
		
		return false;
	}
	
	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		
		sandBoxCount = Integer.parseInt(st.nextToken());
		animalCount = Integer.parseInt(st.nextToken());
		catchLength = Integer.parseInt(st.nextToken());
		
		sandBoxLocation = new int[sandBoxCount];
		st = new StringTokenizer(br.readLine());
		for (int index = 0; index < sandBoxCount; index++) {
			sandBoxLocation[index] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(sandBoxLocation);
		
		animalLocation = new Location[animalCount];
		for (int index = 0; index < animalCount; index++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			animalLocation[index] = new Location(x, y);
		}
		
		int answer = 0;
		for (int animal = 0; animal < animalCount; animal++) {
			if (isCatch(animal)) {
				answer++;
			}
		}
		
		System.out.println(answer);
	}
}