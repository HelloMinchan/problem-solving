# 5:34 ~ 5:42


class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        answer = []

        even_total = 0
        for num in nums:
            if num % 2 == 0:
                even_total += num

        for query in queries:
            val, index = query

            if nums[index] % 2 == 0:
                even_total -= nums[index]

            nums[index] += val

            if nums[index] % 2 == 0:
                even_total += nums[index]

            answer.append(even_total)

        return answer
