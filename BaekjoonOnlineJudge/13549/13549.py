import sys, heapq
input = sys.stdin.readline


def BFS():
    hq = []
    visit[N] = True
    heapq.heappush(hq, (0, N))

    while hq:
        time, now = heapq.heappop(hq)

        for way in range(3):
            if dx[way] == 2:
                future = now * dx[way]

                if future > 100000:
                    continue

                if future == K:
                    return time

                if not visit[future]:
                    visit[future] = True
                    heapq.heappush(hq, (time, future))
            else:
                future = now + dx[way]

                if future < 0 or future > 100000:
                    continue

                if future == K:
                    return time + 1

                if not visit[future]:
                    visit[future] = True
                    heapq.heappush(hq, (time + 1, future))


N, K = map(int, input().split())

if N == K:
    print(0)
    sys.exit(0)

visit = [False] * 100001
dx = [2, -1, 1]

print(BFS())
