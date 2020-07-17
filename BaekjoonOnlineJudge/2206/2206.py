import sys, heapq
input = sys.stdin.readline


def BFS(i, j):
    hq = []
    visit[0][i][j] = True
    heapq.heappush(hq, (1, 0, i, j))
    
    while hq:
        dist, count, i, j = heapq.heappop(hq)

        if i == N - 1 and j == M - 1:
            return dist
            
        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                continue

            if not visit[count][ii][jj]:
                if count < 1:
                    if matrix[ii][jj] == '1':
                        visit[count][ii][jj] = True
                        heapq.heappush(hq, (dist + 1, count + 1, ii, jj))
                    else:
                        visit[count][ii][jj] = True
                        heapq.heappush(hq, (dist + 1, count, ii, jj))
                else:
                    if matrix[ii][jj] == '0':
                        visit[count][ii][jj] = True
                        heapq.heappush(hq, (dist + 1, count, ii, jj))
                        
    return -1


N, M = map(int, (input().split()))
matrix = [list(input().rstrip()) for _ in range(N)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
visit = [[[False] * M for _ in range(N)] for _ in range(2)]

print(BFS(0, 0))
