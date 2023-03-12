class Solution {
    private static int answer = 0;
    private static boolean[] visit;
    
    private static void dfs(int clear, int k, int[][] dungeons) {
        answer = Math.max(answer, clear);
        
        for (int i = 0; i < dungeons.length; i++) {
            if (!visit[i] && k - dungeons[i][0] >= 0) {
                visit[i] = true;
                k -= dungeons[i][1];
                dfs(clear + 1, k, dungeons);
                visit[i] = false;
                k += dungeons[i][1];
            }
        }
    }
    
    public int solution(int k, int[][] dungeons) {
        visit = new boolean[dungeons.length];
        
        dfs(0, k, dungeons);
        
        return answer;
    }
}