import java.io.*;
import java.util.*;

class Query {
	int departure;
	int destination;
	int limitTime;
	
	Query(int departure, int destination, int limitTime) {
		this.departure = departure;
		this.destination = destination;
		this.limitTime = limitTime;
	}
}

class Main {
	private static int N, M;
	private static int[][] adjMatrix;
	private static StringTokenizer st;
	
	private static void floydWarshall() {
		for (int k = 1; k < N + 1; k++) {
			for (int i = 1; i < N + 1; i++) {
				for (int j = 1; j < N + 1; j++) {
					adjMatrix[i][j] = Math.min(adjMatrix[i][j], adjMatrix[i][k] + adjMatrix[k][j]);
				}
			}
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		adjMatrix = new int[N + 1][N + 1];
		
		for (int i = 1; i < N + 1; i++) {
			st = new StringTokenizer(br.readLine());
			
			for (int j = 1; j < N + 1; j++) {
				adjMatrix[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		ArrayList<Query> queries = new ArrayList<>();
		
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int departure = Integer.parseInt(st.nextToken());
			int destination = Integer.parseInt(st.nextToken());;
			int limitTime = Integer.parseInt(st.nextToken());;
			
			queries.add(new Query(departure, destination, limitTime));
		}
		
		floydWarshall();
		
		for (Query query : queries) {
			if (adjMatrix[query.departure][query.destination] <= query.limitTime) {
				System.out.println("Enjoy other party");
			} else {
				System.out.println("Stay here");
			}
		}
	}
}