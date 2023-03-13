import java.util.*;

class Solution {
    private static ArrayList<Integer>[] adjacentList;
    private static int[] distance;
    
    private static void dfs(int node, int move) {
        distance[node] = Math.min(distance[node], move);
        
        for (int nextNode : adjacentList[node]) {
            if (distance[nextNode] > move + 1) {
                dfs(nextNode, move + 1);
            }
        }
    }
    
    public int solution(int n, int[][] edges) {
        int answer = 0;
        
        adjacentList = new ArrayList[n+1];
        for (int i = 0; i < n + 1; i++) {
            adjacentList[i] = new ArrayList<>();
        }
        
        distance = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            distance[i] = Integer.MAX_VALUE;
        }
        
        for (int[] edge : edges) {
            int start = edge[0];
            int end = edge[1];
            
            adjacentList[start].add(end);
            adjacentList[end].add(start);
        }
        
        dfs(1, 0);
        
        int maxDistance = Arrays.stream(distance).filter(d -> d != Integer.MAX_VALUE).max().getAsInt();
        answer = (int) Arrays.stream(distance).filter(d -> d == maxDistance).count();
        
        return answer;
    }
}