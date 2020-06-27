from collections import deque
import sys
input = sys.stdin.readline


def BFS(start, end):
    dq = deque()
    dq.append(start)
    count = 0

    while dq:
        dqSize = len(dq)
        count += 1

        for _ in range(dqSize):
            k, i, j = dq.popleft()

            for way in range(2):
                kk = k + dz[way]

                if kk < 0 or kk > L - 1:
                    continue
                
                if (kk, i, j) == end:
                    return count

                if not visit[kk][i][j] and building[kk][i][j] != '#':
                    visit[kk][i][j] = True
                    dq.append((kk, i, j))
            
            for way in range(4):
                ii = i + dx[way]
                jj = j + dy[way]

                if ii < 0 or ii > R - 1 or jj < 0 or jj > C - 1:
                    continue
                
                if (k, ii, jj) == end:
                    return count
                    
                if not visit[k][ii][jj] and building[k][ii][jj] != '#':
                    visit[k][ii][jj] = True
                    dq.append((k, ii, jj))

    return -1


dx, dy, dz = [0, 0, -1, 1], [-1, 1, 0, 0], [1, -1]

while 1:
    L, R, C = map(int, input().split())
    if L + R + C == 0:
        break

    building = [[] for _ in range(L)]
    for i in range(L):
        for j in range(R):
            building[i].append(list(input().rstrip()))
        input()

    visit = [[[False] * C for _ in range(R)] for _ in range(L)]
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'S':
                    visit[i][j][k] = True
                    start = (i, j, k)
                if building[i][j][k] == 'E':
                    end = (i, j, k)

    time = BFS(start, end)

    if time == -1:
        print("Trapped!")
    else:
        print("Escaped in %d minute(s)." % time)
