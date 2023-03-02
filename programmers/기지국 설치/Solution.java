class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int stationIndex = 0;
        int current = 1;
        
        while(current <= n) {
            // 가장 큰 station의 오른쪽 이거나 station의 왼쪽일 때
            if (stationIndex == stations.length || current < stations[stationIndex] - w) {
                current += 2 * w + 1;
                answer++;
            }
            // station의 범위 안일 때
            else if (stations[stationIndex] - w <= current && current <= stations[stationIndex] + w) {
                current = stations[stationIndex] + w + 1;
                stationIndex++;
            }
            // station의 오른쪽일 때
            else {
                stationIndex++;
            }
        }
        
        return answer;
    }
}