import java.util.*;

class Solution {
    public int solution(String dartResult) {
        dartResult = dartResult.replace("10", "x");
        int answer = 0;
        
        ArrayList<Integer> scoreList = new ArrayList<>();
        
        int i = 0;
        while (i < dartResult.length()) {
            int scoreIndex = scoreList.size() - 1;
            
            switch (dartResult.charAt(i)) {
                case 'S':
                    scoreList.set(scoreIndex, (int) Math.pow(scoreList.get(scoreIndex), 1));
                    break;
                case 'D':
                    scoreList.set(scoreIndex, (int) Math.pow(scoreList.get(scoreIndex), 2));
                    break;
                case 'T':
                    scoreList.set(scoreIndex, (int) Math.pow(scoreList.get(scoreIndex), 3));
                    break;
                case '*':
                    if (scoreIndex < 1) {
                        scoreList.set(scoreIndex, scoreList.get(scoreIndex) * 2);
                    } else {
                        scoreList.set(scoreIndex, scoreList.get(scoreIndex) * 2);
                        scoreList.set(scoreIndex - 1, scoreList.get(scoreIndex - 1) * 2);
                    }
                    break;
                case '#':
                    scoreList.set(scoreIndex, scoreList.get(scoreIndex) * -1);
                    break;
                case 'x':
                    scoreList.add(10);
                    break;
                default:
                    scoreList.add(Character.getNumericValue(dartResult.charAt(i)));
            }
            
            i++;
        }
        
        return scoreList.stream().mapToInt(Integer::valueOf).sum();
    }
}