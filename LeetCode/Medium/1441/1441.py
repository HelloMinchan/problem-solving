class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_index = 0
        number = 1
        answer = []

        while True:
            if len(target) <= target_index:
                return answer

            if target[target_index] == number:
                answer.append("Push")
                target_index += 1
                number += 1
            else:
                answer.append("Push")
                answer.append("Pop")
                number += 1
