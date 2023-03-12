class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        for (int width = 1; width <= 5000; width++) {
            for (int height = 1; height <= 5000; height++) {
                if (brown == (width - 2) * 2 + (height - 2) * 2 + 4 && yellow == (width - 2) * (height - 2)) {
                    answer[0] = width;
                    answer[1] = height;
                }
            }
        }
        
        return answer;
    }
}