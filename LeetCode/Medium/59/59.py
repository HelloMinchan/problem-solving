# 4:10 ~ 4:36


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        matrix = [[0 for _ in range(n)] for _ in range(n)]

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        WAY_LENGTH = 4
        way = 0

        i = 0
        j = 0
        value = 1

        while True:
            matrix[i][j] = value

            i = i + dx[way]
            j = j + dy[way]

            # 테두리 바깥으로 넘어 간 경우
            if i < 0 or i > n - 1 or j < 0 or j > n - 1:
                i = i - dx[way]
                j = j - dy[way]

                way = (way + 1) % WAY_LENGTH

                i = i + dx[way]
                j = j + dy[way]

            # 이미 숫자가 칠해진 경우
            if matrix[i][j] != 0:
                is_end = True

                i = i - dx[way]
                j = j - dy[way]

                # 상 확인
                if i - 1 >= 0:
                    if matrix[i - 1][j] == 0:
                        is_end = False

                # 하 확인
                if i + 1 <= n - 1:
                    if matrix[i + 1][j] == 0:
                        is_end = False

                # 좌 확인
                if j - 1 >= 0:
                    if matrix[i][j - 1] == 0:
                        is_end = False

                # 우 확인
                if j + 1 <= n - 1:
                    if matrix[i][j + 1] == 0:
                        is_end = False

                if is_end:
                    break
                else:
                    way = (way + 1) % WAY_LENGTH

                    i = i + dx[way]
                    j = j + dy[way]

            value += 1

        return matrix
