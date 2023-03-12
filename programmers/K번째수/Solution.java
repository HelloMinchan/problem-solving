import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        final int COMMAND_LENGTH = commands.length;
        
        int[] answer = new int[COMMAND_LENGTH];
        
        for (int commandIndex = 0; commandIndex < COMMAND_LENGTH; commandIndex++) {
            int[] command = commands[commandIndex];
            
            ArrayList<Integer> slice = new ArrayList<>();
            
            for (int arrayIndex = command[0] - 1; arrayIndex < command[1]; arrayIndex++) {
                slice.add(array[arrayIndex]);
            }
            
            Collections.sort(slice);
            
            answer[commandIndex] = slice.get(command[2] - 1);
        }
        
        return answer;
    }
}