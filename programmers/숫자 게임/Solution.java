import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        
        Arrays.sort(A);
        
        PriorityQueue<Integer> pQ = new PriorityQueue<>();
        for (int number : B) {
            pQ.add(number);
        }
           
        for (int aNumber: A) {
            while (!pQ.isEmpty() && pQ.peek() <= aNumber) {
                pQ.poll();
            }

            if (!pQ.isEmpty()) {
                pQ.poll();
                answer++;
            } else {
                break;
            }
        }
        
        return answer;
    }
}