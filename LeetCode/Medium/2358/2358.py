class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        length = len(grades)

        answer = 1

        while True:
            length -= answer
            answer += 1

            if length < answer:
                break

        return answer - 1
