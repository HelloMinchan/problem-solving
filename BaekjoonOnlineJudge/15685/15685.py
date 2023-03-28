import sys

input = sys.stdin.readline

N = int(input())

MAX_SIZE = 101

board = [[False for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(N):
    y, x, d, g = map(int, input().split())

    board[x][y] = True

    ways = [d]
    for _ in range(g):
        for way in ways[::-1]:
            ways.append((way + 1) % 4)

    for way in ways:
        x += dx[way]
        y += dy[way]

        if x < 0 or x >= MAX_SIZE or y < 0 or y >= MAX_SIZE:
            continue

        board[x][y] = True

answer = 0
for i in range(MAX_SIZE - 1):
    for j in range(MAX_SIZE - 1):
        if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
            answer += 1

print(answer)
