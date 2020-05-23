import sys, queue
input = sys.stdin.readline


def BFS(q):
    global K, visit, dx, time

    while not q.empty():
        size = q.qsize()

        for _ in range(size):
            x = q.get()
            
            if x == K:
                print(time)
                exit()
            
            if visit[x] == False:
                visit[x] = True

                for way in range(3):
                    if way == 2:
                        ii = x * dx[way]
                    else:
                        ii = x + dx[way]

                    if ii < 0 or ii > 100000:
                        continue
                    
                    q.put(ii)
        time += 1
        

N, K = map(int, input().split())
visit = [False] * 100001
dx = [-1, 1, 2]
time = 0

q = queue.Queue()
q.put(N)

BFS(q)