class Solution:
    def frequencySort(self, s: str) -> str:
        d = dict()

        for char in s:
            if d.get(char, None):
                d[char] += 1
            else:
                d[char] = 1

        answer = ""
        for char_tuple in sorted(d.items(), key=lambda x: x[1], reverse=True):
            for _ in range(char_tuple[1]):
                answer += char_tuple[0]

        return answer
