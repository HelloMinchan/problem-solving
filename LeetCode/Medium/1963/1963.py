class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []

        for bracket in s:
            if bracket == "[":
                stack.append(bracket)
            else:
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append(bracket)

        swaps = len(stack) // 2

        return swaps // 2 if swaps % 2 == 0 else swaps // 2 + 1
