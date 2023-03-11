import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, Integer> clothMap = new HashMap<>();
        
        for (String[] cloth : clothes) {
            clothMap.put(cloth[1], clothMap.getOrDefault(cloth[1], 0) + 1);
        }
        
        for (int clothCount : clothMap.values()) {
            answer *= clothCount + 1;
        }
        return answer - 1;
    }
}