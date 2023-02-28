import java.util.*;

class Solution {
    public long solution(int n, int[] remainWorkWeights) {
        long answer = 0;
        
        PriorityQueue<Integer> maxRemainWorkWeightQueue = new PriorityQueue<>(Collections.reverseOrder());
        
        for (int remainWorkWeight :remainWorkWeights) {
            maxRemainWorkWeightQueue.add(remainWorkWeight);
        }
        
        while (!maxRemainWorkWeightQueue.isEmpty() && n-- != 0) {
            int currentWorkweight = maxRemainWorkWeightQueue.poll();
            currentWorkweight--;
            
            if (currentWorkweight > 0) {
                maxRemainWorkWeightQueue.add(currentWorkweight);    
            }
        }
        
        while (!maxRemainWorkWeightQueue.isEmpty()) {
            answer += Math.pow(maxRemainWorkWeightQueue.poll(), 2);
        }
        
        return answer;
    }
}