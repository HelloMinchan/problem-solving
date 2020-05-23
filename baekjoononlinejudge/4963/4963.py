import sys, queue
input = sys.stdin.readline


def BFS(i, j):
    global w, h, MAP, visit, dx, dy, island
    island += 1

    q = queue.Queue()
    q.put((i, j))

    while q.qsize():
        x, y = q.get()

        if visit[x][y] == False:
            visit[x][y] = True
            for way in range(8):
                ii, jj = x + dx[way], y + dy[way]

                if ii < 0 or ii > h - 1 or jj < 0 or jj > w - 1:
                    continue

                if MAP[ii][jj] == 1:
                    q.put((ii, jj))


while True:
    w, h = map(int, input().split())
    if not w + h:
        exit()
    
    MAP = [list(map(int, input().split())) for _ in range(h)]
    visit = [[False] * w for _ in range(h)]
    dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
    island = 0

    for i in range(h):
        for j in range(w):
            if MAP[i][j] == 1 and visit[i][j] == False:
                BFS(i, j)
    
    print(island)