import sys, heapq

input = sys.stdin.readline

def bfs(hq):
    while hq:
        time, location = heapq.heappop(hq)

        if location == K:
            print(time)
            return

        for way in range(3):
            if way == 2:
                next_location = location * way
            else:
                next_location = location + dx[way]
            
            if next_location < -100000 or next_location > 100000:
                continue

            if not visit[next_location]:
                visit[next_location] = True

                heapq.heappush(hq, (time+1, next_location))


N, K = map(int, input().split())
visit = [0 for _ in range(200001)]

dx = [-1, 1]

hq = []
heapq.heappush(hq, (0, N))

bfs(hq)