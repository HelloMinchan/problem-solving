import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        int[] answer = {1, gems.length};
               
        Set<String> gemType = new HashSet<>();
        for (String gem : gems) {
            gemType.add(gem);
        }
        
        if (gems.length == 1 || gemType.size() == 1) {
            answer[0] = 1;
            answer[1] = 1;
            return answer;
        }
        
        int moveI = 0;
        int moveJ = 1;
        Map<String, Integer> buyType = new HashMap<>();
        buyType.put(gems[moveI], 1);
        buyType.put(gems[moveJ], 1);
        
        while (true) {
            if (buyType.keySet().size() == gemType.size()) {
                if (answer[1] - answer[0] > moveJ - moveI) {
                    answer[1] = moveJ + 1;
                    answer[0] = moveI + 1;
                }
                
                if (moveI + 1 < moveJ) {
                    System.out.println(buyType.getOrDefault(gems[moveI], 0));
                    if (buyType.getOrDefault(gems[moveI], 0) > 1) {
                        buyType.put(gems[moveI], buyType.get(gems[moveI]) - 1);
                    } else {
                        buyType.remove(gems[moveI]);
                    }
                    moveI++;
                } else {
                    if (moveJ + 1 < gems.length) {
                        buyType.put(gems[moveJ + 1], buyType.getOrDefault(gems[moveJ + 1], 0) + 1);
                        moveJ++;
                    } else {
                        break;
                    }
                }
            } else {
                if (moveJ + 1 < gems.length) {
                    buyType.put(gems[moveJ + 1], buyType.getOrDefault(gems[moveJ + 1], 0) + 1);
                    moveJ++;
                } else {
                    if (moveI + 1 < gems.length) {
                        if (buyType.get(gems[moveI]) > 1) {
                            buyType.put(gems[moveI], buyType.get(gems[moveI]) - 1);
                        } else {
                            buyType.remove(gems[moveI]);
                        }
                        moveI++;
                    } else {
                        break;
                    }
                }
            }
        }            

        return answer;
    }
}