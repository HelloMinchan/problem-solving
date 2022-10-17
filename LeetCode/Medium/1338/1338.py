class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        length = len(arr)

        d = dict()

        for num in arr:
            if d.get(num, 0):
                d[num] += 1
            else:
                d[num] = 1

        answer = 0
        for count in list(sorted(d.values(), reverse=True)):
            length -= count
            answer += 1

            if len(arr) // 2 >= length:
                break

        return answer
