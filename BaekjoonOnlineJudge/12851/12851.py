from collections import deque
import sys
input = sys.stdin.readline


def BFS():
    dq = deque()
    dq.append(N)

    isPossible = True
    time = 0
    count = 0
    while dq and isPossible:
        dqSize = len(dq)
        time += 1

        for _ in range(dqSize):
            now = dq.popleft()
            visit[now] = True

            for way in range(3):
                if dx[way] == 2:
                    future = now * 2
                else:
                    future = now + dx[way]

                if future < 0 or future > 100000:
                    continue
                
                if future == K:
                    isPossible = False
                    count += 1
                    continue

                if not visit[future]:
                    dq.append(future)

    return time, count


N, K = map(int, input().split())

if N == K:
    print(0)
    print(1)
    sys.exit(0)

visit = [False] * 100001
dx = [2, -1, 1]

time, count = BFS()

print(time)
print(count)
