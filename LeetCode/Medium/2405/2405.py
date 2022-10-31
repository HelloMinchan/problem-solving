class Solution:
    def partitionString(self, s: str) -> int:
        answer = 0

        substring = dict()
        for char in s:
            if substring.get(char, 0):
                answer += 1
                substring = dict()
                substring[char] = 1
            else:
                substring[char] = 1

        if substring:
            answer += 1

        return answer
