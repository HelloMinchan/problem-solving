class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int h = triangle.length;
        
        for(int i=1;i<h;i++) {
            int w = triangle[i].length;
            for(int j=0;j<w;j++) {
                if(i==1)
                    triangle[i][j]=triangle[i][j]+triangle[i-1][0];
                else {
                    if(j==0)
                        triangle[i][j]=triangle[i][j]+triangle[i-1][0];
                    else if(j==w-1)
                        triangle[i][j]=triangle[i][j]+triangle[i-1][(triangle[i-1].length)-1];
                    else {
                        if(triangle[i][j]+triangle[i-1][j-1]>triangle[i][j]+triangle[i-1][j])
                            triangle[i][j]=triangle[i][j]+triangle[i-1][j-1];
                        else
                            triangle[i][j]=triangle[i][j]+triangle[i-1][j];
                    }
                }
            }
        }
        
        for(int i=0;i<triangle[h-1].length;i++)
            if(answer<triangle[h-1][i])
                answer=triangle[h-1][i];
        
        return answer;
    }
}
