import java.util.*;

class Solution {
    public int[] solution(String msg) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        int dictNumber = 1;
        Map<String, Integer> dict = new HashMap<>();
        
        for (int i = 0; i < 26; i++) {
            dict.put(String.valueOf((char) ('A' + i)), dictNumber++);
        }
        
        int i = 0;
        while (i < msg.length()) {
            StringBuilder sb = new StringBuilder();
            sb.append(msg.charAt(i));
            
            int j = i;
            while (dict.containsKey(sb.toString())) {
                j++;
                if (j > msg.length() - 1) {
                    break;
                }
                
                sb.append(msg.charAt(j));
            }
            i += j - i;
            
            if (i > msg.length() - 1) {
                answer.add(dict.get(sb.toString()));
            } else {
                dict.put(sb.toString(), dictNumber++);
                answer.add(dict.get(sb.deleteCharAt(sb.length() - 1).toString()));
            }
        }
        
        
        return answer.stream().mapToInt(Integer::valueOf).toArray();
    }
}