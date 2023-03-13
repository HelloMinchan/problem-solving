import java.io.*;
import java.util.*;

class Location {
	int move;
	int i;
	int j;
	
	Location (int move, int i, int j) {
		this.move = move;
		this.i = i;
		this.j = j;
	}
}

class Main {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static StringTokenizer st;
	
	private static int h, w;
	private static char[][] map;
	private static int[][] distance;
	
	private static final char WALL = '#';
	private static final char EMPTY = '.';
	private static final char START = 'S';
	private static final char END = 'E';
	
	private static int[] dx = {0, 0, -1, 1};
	private static int[] dy = {-1, 1, 0, 0};
	private static final int WAY_COUNT = 4;
	
	private static PriorityQueue<Location> locationQueue = new PriorityQueue<>((l1, l2) -> l1.move - l2.move);
	
	private static boolean checkAroundWall(int i, int j) {
		for (int way = 0; way < WAY_COUNT; way++) {
			int aroundI = i + dy[way];
			int aroundJ = j + dx[way];
			
			if (aroundI < 0 || aroundI > h - 1 || aroundJ < 0 || aroundJ > w - 1) {
				continue;
			}
			
			if (map[aroundI][aroundJ] == WALL) {
				return true;
			}
		}
		
		return false;
	}
	
	private static int dijkstra() {
		int answer = 0;
		
		while (!locationQueue.isEmpty()) {
			Location current = locationQueue.poll();
			
			if (map[current.i][current.j] == END) {
				answer = current.move;
			}
			
			boolean isWallSide = checkAroundWall(current.i, current.j);
			
			for (int way = 0; way < WAY_COUNT; way++) {
				int nextI = current.i + dy[way];
				int nextJ = current.j + dx[way];
				
				if (nextI < 0 || nextI > h - 1 || nextJ < 0 || nextJ > w - 1) {
					continue;
				}
				
				boolean isNextWallSide = checkAroundWall(nextI, nextJ);
				
				if (isWallSide && isNextWallSide) {
					if (distance[nextI][nextJ] > current.move && map[nextI][nextJ] != WALL) {
						distance[nextI][nextJ] = current.move;
						locationQueue.add(new Location(current.move, nextI, nextJ));	
					} 
				} else {
					if (distance[nextI][nextJ] > current.move + 1 && map[nextI][nextJ] != WALL) {
						distance[nextI][nextJ] = current.move + 1;
						locationQueue.add(new Location(current.move + 1, nextI, nextJ));	
					} 
				}
			}
		}
		
		return answer;
	}
	
	public static void main(String[] args) throws Exception {
		st = new StringTokenizer(br.readLine());
		
		h = Integer.parseInt(st.nextToken());
		w = Integer.parseInt(st.nextToken());
		
		map = new char[h][w];
		distance = new int[h][w];
		for (int i = 0; i < h; i++) {
			Arrays.fill(distance[i], Integer.MAX_VALUE);	
		}
		
		for (int i = 0; i < h; i++) {
			String row = br.readLine();
			
			for (int j = 0; j < w; j++) {
				map[i][j] = row.charAt(j);
				
				if (map[i][j] == START) {
					distance[i][j] = -1;
					locationQueue.add(new Location(0, i, j));
				}
			}
		}
		
		System.out.println(dijkstra());
	}
}