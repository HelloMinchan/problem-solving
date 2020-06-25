from collections import deque
import sys
input = sys.stdin.readline


def BFS(cur, visit):
    dq = deque()
    dq.append((cur, visit))
    count = 0

    while dq:
        dqSize = len(dq)
        count += 1

        for _ in range(dqSize):
            cur, visit = dq.popleft()

            for way in range(4):
                if cur % 3 == 0:
                    if dx[way] == -1:
                        continue
                if cur % 3 == 2:
                    if dx[way] == 1:
                        continue

                nextCur = cur + dx[way]

                if nextCur < 0 or nextCur > 8:
                    continue
                
                temp = list(visit)
                temp[cur], temp[nextCur] = temp[nextCur], temp[cur]
                temp = "".join(temp)

                if temp == "123456780":
                    return count

                if not memoization.get(temp, 0):
                    memoization[temp] = 1
                    dq.append((nextCur, temp))
    return -1


puzzle = [list(map(str, input().split())) for _ in range(3)]
memoization = dict()
dx = [-1, +1, -3, 3]

cur = 0
visit = ""
for i in range(3):
    for j in range(3):
        if puzzle[i][j] == '0':
            cur = j + (3 * i)
        visit += puzzle[i][j]

if visit == "123456780":
    print(0)
    sys.exit(0)

memoization[visit] = 1
print(BFS(cur, visit))
