import java.util.*;

class Solution {
    public String solution(String[] participants, String[] completions) {
        String answer = "";
        
        Map<String, Integer> participantMap = new HashMap<>();
        
        for (String participant : participants) {
            participantMap.put(participant, participantMap.getOrDefault(participant, 0) + 1);
        }
        
        for (String completion : completions) {
            participantMap.put(completion, participantMap.get(completion) - 1);
        }
        
        for (Map.Entry<String, Integer> participant : participantMap.entrySet()) {
            if (participant.getValue() > 0) {
                answer = participant.getKey();
            }
        }
        
        return answer;
    }
}