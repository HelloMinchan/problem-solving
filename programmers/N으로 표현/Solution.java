import java.util.*;

class Solution {
    private static Map<Long, Integer> memoization = new HashMap<>();
    private static int answer = Integer.MAX_VALUE;
    
    private static void dfs(int count, int N, long currentNumber, int number) {
        if (count > 8) {
            return;
        }
        
        if (memoization.containsKey(currentNumber)) {
            if (memoization.get(currentNumber) <= count) {
                return;
            }
        }
        
        if (currentNumber == number) {
            answer = Math.min(answer, count);
            return;
        }
        
        memoization.put(currentNumber, count);
        
        int operValue = 0;
        for (int i = 0; i < 8; i++) {
            if (count + i < 8) {
                operValue = operValue * 10 + N;
                int nextCount = count + i + 1;
                dfs(nextCount, N, currentNumber + operValue, number);
                dfs(nextCount, N, currentNumber - operValue, number);
                dfs(nextCount, N, currentNumber / operValue, number);
                dfs(nextCount, N, currentNumber * operValue, number);
            }
        }
    }
    
    public int solution(int N, int number) {
        dfs(0, N, 0, number);
        
        if (answer == Integer.MAX_VALUE) {
            return - 1;
        }
        return answer;
    }
}