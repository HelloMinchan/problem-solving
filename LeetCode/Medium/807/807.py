class Solution:

    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        tot = 0
        
        lrSkyline = [max(height) for height in grid]
        udSkyline = [max(height) for height in zip(*grid)]
            
        for i, arr in enumerate(grid):
            for j, height in enumerate(arr):
                limit = min(lrSkyline[i], udSkyline[j])
                if limit > height:
                    tot += limit - height
                    
        return tot