import java.util.*;

class Solution {
    private static boolean[] visit;
    private static Stack<Integer> stack = new Stack<>();
    private static boolean[] isPrimeNumber = new boolean[10000001];
    private static Set<Integer> candidates = new HashSet<>();
    
    private static void primeNumberSetting() {
        isPrimeNumber[0] = isPrimeNumber[1] = true;
        
         for (int i = 2; i * i < isPrimeNumber.length; i++){
            if (!isPrimeNumber[i]) {
            	for (int j = i * i; j < isPrimeNumber.length; j+=i) {
                    isPrimeNumber[j] = true;
                }
            }        
        }
    }
    
    private static void dfs(String numbers) {
        if (!stack.isEmpty()) {
            StringBuilder sb = new StringBuilder();
            for (int number : stack) {
                sb.append(number);    
            }
            
           candidates.add(Integer.parseInt(sb.toString()));
        }
        
        for (int i = 0; i < numbers.length(); i++) {
            if (!visit[i]) {
                visit[i] = true;
                stack.add(numbers.charAt(i) - '0');
                dfs(numbers);
                visit[i] = false;
                stack.pop();
            }
        }
    }
    
    public int solution(String numbers) {
        int answer = 0;
        visit = new boolean[numbers.length()];
        primeNumberSetting();
        dfs(numbers);
        
        for (int candidate : candidates) {
            if (!isPrimeNumber[candidate]) {
                answer++;
            }
        }
        
        return answer;
    }
}