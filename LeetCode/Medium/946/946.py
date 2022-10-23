# 5:15 ~ 5 : 31


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        push_index = 0
        pop_index = 0

        while True:
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1

            stack.append(pushed[push_index])
            push_index += 1

            if push_index == len(pushed):
                break

        while True:
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1

                if pop_index == len(popped):
                    return True

            return False
