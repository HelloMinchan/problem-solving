import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        Map<Integer, Integer> score = new HashMap<>();
        Map<Integer, Integer[]> answerSet = new HashMap<>();
        Integer[] answerSet1 = {1, 2, 3, 4, 5};
        Integer[] answerSet2 = {2, 1, 2, 3, 2, 4, 2, 5};
        Integer[] answerSet3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        answerSet.put(1, answerSet1);
        answerSet.put(2, answerSet2);
        answerSet.put(3, answerSet3);
        
        for (int i = 0; i < answers.length; i++) {
            for (int person = 1; person <= 3; person++) {
                if (answers[i] == answerSet.get(person)[i % answerSet.get(person).length]) {
                    score.put(person, score.getOrDefault(person, 0) + 1);
                }    
            }
        }
        
        int maxScore = score.values().stream().mapToInt(i->i).max().getAsInt();
        
        for (Map.Entry<Integer, Integer> scoreEntry : score.entrySet()) {
            if (scoreEntry.getValue() == maxScore) {
                answer.add(scoreEntry.getKey());
            }
        }
        
        return answer.stream().mapToInt(i->i).toArray();
    }
}