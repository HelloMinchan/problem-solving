import sys, heapq

input = sys.stdin.readline

def bfs(hq):
    while hq:
        t, now = heapq.heappop(hq)

        if now == K:
            print(t)
            return

        if now + 1 <= 100000 and now + 1 >= -100000:
            if not visit[now+1]:
                visit[now+1] = True
                heapq.heappush(hq, (t+1, now+1))
        if now - 1 <= 100000 and now - 1 >= -100000:
            if not visit[now-1]:
                visit[now-1] = True
                heapq.heappush(hq, (t+1, now-1))
        if now * 2 <= 100000 and now * 2 >= -100000:
            if not visit[now*2]:
                visit[now*2] = True
                heapq.heappush(hq, (t+1, now*2))


N, K = map(int,input().split())

visit = [False for _ in range(200001)]
hq = []
heapq.heappush(hq, (0, N))

bfs(hq)