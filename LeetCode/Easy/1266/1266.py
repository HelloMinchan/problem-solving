class Solution:

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        pre = points[0]
        
        for i in range(1, len(points)):
            a = abs(pre[0] - points[i][0])
            b = abs(pre[1] - points[i][1])
            if a > b:
                count += a
            else:
                count += b
            pre = points[i]
            
        return count