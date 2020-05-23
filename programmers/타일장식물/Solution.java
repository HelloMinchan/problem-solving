class Solution {
    public long solution(int N) {
        long answer = 0;
        long[] fibo = new long[N+1];
        long[] table = new long[N+1];
        
        for(int i=1;i < fibo.length;i++) {
            if(i==1)
                fibo[1]=1;
            else if(i==2)
                fibo[2]=2;
            else
                fibo[i]=fibo[i-1]+fibo[i-2];
        }
        
        for(int i=1;i<table.length;i++)
            table[i]=((fibo[i]+fibo[i-1])*2)+(2*fibo[i]);
        
        answer = table[N-1];
        return answer;
    }
}
