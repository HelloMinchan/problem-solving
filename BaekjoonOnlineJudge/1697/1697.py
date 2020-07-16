from collections import deque
import sys
input = sys.stdin.readline


def BFS(x):
    dq = deque()
    visit[x] = True
    dq.append((x, 0))

    while dq:
        x, time = dq.popleft()

        if x == K:
            return time
        
        for way in range(3):
            if way == 2:
                xx = x * 2
            else:
                xx = x + dx[way]
            
            if xx < 0 or xx > 100000:
                continue

            if not visit[xx]:
                visit[xx] = True
                dq.append((xx, time + 1))


N, K = map(int, input().split())

visit = [False] * 100001
dx = [-1, 1, 2]

print(BFS(N))
