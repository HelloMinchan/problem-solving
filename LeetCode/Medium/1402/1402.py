class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        answer = 0
        total = 0
        satisfaction.sort()

        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            answer += total

        return answer
