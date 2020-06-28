from collections import deque
import sys
input = sys.stdin.readline


def BFS():
    dq = deque()
    visit[N] = True
    dq.append((N, 0))

    while dq:
        now, time = dq.popleft()

        for way in range(3):
            if dx[way] == 2:
                future = now * 2

                if future > 100000:
                    continue
            else:
                future = now + dx[way]

                if future < 0 or future > 100000:
                    continue

            if future == K:
                beforeRecord[future] = now
                return time + 1, future
            
            if not visit[future]:
                visit[future] = True
                beforeRecord[future] = now
                dq.append((future, time + 1))


N, K = map(int, input().split())

if N == K:
    print(0)
    print(N)
    sys.exit(0)

visit = [False] * 100001
beforeRecord = [0] * 100001
beforeRecord[N] = -1
dx = [2, -1, 1]

time, future = BFS()

history = [future]
while 1:
    if beforeRecord[future] == -1:
        break
    history.append(beforeRecord[future])
    future = beforeRecord[future]

print(time)
print(*reversed(history))
