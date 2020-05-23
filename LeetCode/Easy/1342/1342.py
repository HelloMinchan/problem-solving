class Solution:

    def numberOfSteps (self, num: int) -> int:
        count = 0
        while True:
            if num == 0:
                break
            elif num % 2 == 0:
                count += 1
                num = num / 2
            else:
                count += 1
                num = num - 1
        return count