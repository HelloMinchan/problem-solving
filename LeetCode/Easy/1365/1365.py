class Solution:

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        li = [0] * (max(nums) + 1)
        for i in nums:
            li[i] = (nums.count(i))
        res = [sum(li[:x]) for x in nums]
        
        return res