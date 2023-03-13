import java.util.*;

class Solution {
    private static final int MOD_VALUE = 1000000007;
    private static int[][] map;
    
    private static int dfs(int i, int j, int n, int m) {
        if (map[i][j] == -1) {
            return 0;
        }
        
        if (i == n && j == m) {
            map[i][j] = 1;
            return map[i][j];
        }
        
        if (map[i][j] != 0) {
            return map[i][j];
        }
        
        if (i + 1 <= n) {
            map[i][j] += dfs(i + 1, j, n, m);    
        }
        if (j + 1 <= m) {
            map[i][j] += dfs(i, j + 1, n, m);    
        }
        
        map[i][j] %= MOD_VALUE;
        
        return map[i][j];
    }
    
    public int solution(int m, int n, int[][] puddles) {
        map = new int[n + 1][m + 1];
        
        for (int[] puddle : puddles) {
            map[puddle[1]][puddle[0]] = -1;
        }
        
        return dfs(1, 1, n, m);
    }
}