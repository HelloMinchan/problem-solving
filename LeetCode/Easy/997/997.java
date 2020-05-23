class Solution {
    public int findJudge(int N, int[][] trust) {
        if(N==1)
            return 1;
        
        int[] table1 = new int[N+1];
        int[] table2 = new int[N+1];
        
        int temp =0;
        
        for(int i=0;i<trust.length;i++) {
            table1[trust[i][1]]++;
            table2[trust[i][0]]++;
        }
        
        for(int i=0;i<N+1;i++)
            if(table1[i]==N-1&&table2[i]==0)
                return i;
        
        return -1;
    }
}
