# 7:06 ~ 7:31 (25분)
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp_table = [[0 for _ in range(n)] for _ in range(2)]

    for j in range(n):
        for i in range(2):
            if j == 0:
                dp_table[i][j] = stickers[i][j]
            elif j == 1:
                if i == 0:
                    dp_table[i][j] = stickers[i][j] + dp_table[1][j - 1]
                else:
                    dp_table[i][j] = stickers[i][j] + dp_table[0][j - 1]
            else:
                if i == 0:
                    dp_table[i][j] = stickers[i][j] + max(
                        dp_table[1][j - 1], dp_table[1][j - 2]
                    )
                else:
                    dp_table[i][j] = stickers[i][j] + max(
                        dp_table[0][j - 1], dp_table[0][j - 2]
                    )

    print(max(max(dp_table[-1]), max(dp_table[-2])))