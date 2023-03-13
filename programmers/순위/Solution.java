import java.util.*;

class Solution {
    private static int[][] resultTable;
    private static void floydWarshall(int n) {
        for (int playerA = 1; playerA <= n; playerA++) {
            for (int playerB = 1; playerB <= n; playerB++) {
                for (int playerC = 1; playerC <= n; playerC++) {
                    if (resultTable[playerA][playerB] == 1 && resultTable[playerB][playerC] == 1) {
                        resultTable[playerA][playerC] = 1;
                        resultTable[playerC][playerA] = -1;
                    }
                    if (resultTable[playerA][playerB] == -1 && resultTable[playerB][playerC] == -1) {
                        resultTable[playerA][playerC] = -1;
                        resultTable[playerC][playerA] = 1;
                    }
                }
            }
        }
    }
    
    public int solution(int n, int[][] results) {
        int answer = 0;
        resultTable = new int[n+1][n+1];
        
        for (int[] result : results) {
            int playerA = result[0];
            int playerB = result[1];
            
            resultTable[playerA][playerB] = 1;
            resultTable[playerB][playerA] = -1;
        }
        
        floydWarshall(n);
        
        for (int playerA = 1; playerA <= n; playerA++) {
            int rankCount = 0;
            
            for (int playerB = 1; playerB <= n; playerB++) {
                if (resultTable[playerA][playerB] != 0) {
                    rankCount++;
                }
            }
            
            if (rankCount == n - 1) {
                answer++;
            }
        }
    
        return answer;
    }
}