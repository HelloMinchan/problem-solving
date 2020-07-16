from collections import deque
import sys
input = sys.stdin.readline


def BFS(i, j):
    dq = deque()
    dq.append((i, j))
    
    count = 0

    while dq:
        i, j = dq.popleft()
        count += 1

        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > N - 1 or jj < 0 or jj > N - 1:
                continue

            if not visit[ii][jj] and MAP[ii][jj] == '1':
                visit[ii][jj] = True
                dq.append((ii, jj))
    
    return count


N = int(input())
MAP = [list(input().rstrip()) for _ in range(N)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
answer = []
visit = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if MAP[i][j] == '1' and not visit[i][j]:
            visit[i][j] = True
            answer.append(BFS(i, j))

answer.sort()
print(len(answer))

for count in answer:
    print(count)
