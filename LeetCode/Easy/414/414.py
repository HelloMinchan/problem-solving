class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        max = nums[0]
        if len(nums) < 3:
            return(max)
        
        n = 0
        for i in range(1, len(nums)):
            if n == 2:
                break
            elif max > nums[i]:
                max = nums[i]
                n += 1
        if n != 2:
            return nums[0]
        else:
            return(max)
