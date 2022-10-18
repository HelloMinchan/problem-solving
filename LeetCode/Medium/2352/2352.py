class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = list(zip(*grid))
        answer = 0

        for rows in grid:
            for col in range(len(rows)):
                if rows == list(cols[col]):
                    answer += 1

        return answer
