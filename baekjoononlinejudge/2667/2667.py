import sys, queue
input = sys.stdin.readline


def BFS(i, j):
    global N, house, dx, dy, visit, district
    count = 0
    q = queue.Queue()
    q.put((i, j))

    while q.qsize():
        x, y = q.get()

        if visit[x][y] == False:
            visit[x][y] = True
            count += 1
            for way in range(4):
                ii, jj = x + dx[way], y + dy[way]
                if ii < 0 or ii > N - 1 or jj < 0 or jj > N - 1:
                    continue
                if house[ii][jj] == 1:
                    q.put((ii, jj))
    district.append(count)


N = int(input())
house = [list(map(int, input().rstrip())) for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
visit = [[False] * N for _ in range(N)]
district = []

for i in range(N):
    for j in range(N):
        if house[i][j] == 1 and visit[i][j] == False:
            BFS(i, j)

print(len(district))
print(*(sorted(district)), sep="\n")