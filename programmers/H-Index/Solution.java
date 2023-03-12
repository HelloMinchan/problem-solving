class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        while (true) {
            int count = 0;
            for (int citation : citations) {
                if (citation >= answer) {
                    count++;
                }
            }
            if (count >= answer && (citations.length - count) <= answer) {
                answer++;
            } else {
                break;
            }
        }
        
        return answer - 1;
    }
}