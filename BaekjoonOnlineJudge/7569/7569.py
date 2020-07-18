from collections import deque
import sys
input = sys.stdin.readline


def BFS():
    global unRipedTomato

    day = -1

    while dq:
        dqSize = len(dq)
        day += 1

        for _ in range(dqSize):
            k, i, j = dq.popleft()

            # 위, 아래 검사
            for way in range(2):
                kk = k + dz[way]

                if kk < 0 or kk > H - 1:
                    continue

                if not visit[kk][i][j] and box[kk][i][j] != -1:
                    visit[kk][i][j] = True
                    unRipedTomato -= 1
                    dq.append((kk, i, j))
            
            # 동, 서, 남, 북 검사
            for way in range(4):
                ii = i + dx[way]
                jj = j + dy[way]

                if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                    continue

                if not visit[k][ii][jj] and box[k][ii][jj] != -1:
                    visit[k][ii][jj] = True
                    unRipedTomato -= 1
                    dq.append((k, ii, jj))
    
    return day


M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visit = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
dx, dy, dz = [0, 0, -1, 1], [-1, 1, 0, 0], [-1, 1]

unRipedTomato = 0
dq = deque()

for k in range(H):
    for i in range(N):
        for j in range(M):
            if box[k][i][j] == 0:
                unRipedTomato += 1
            elif box[k][i][j] == 1:
                visit[k][i][j] = True
                dq.append((k, i, j))

answer = BFS()

if unRipedTomato:
    print(-1)
else:
    print(answer)
