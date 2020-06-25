from collections import deque
import sys
input = sys.stdin.readline


def BFS(p):
    dq = deque()
    dq.append(p)

    count = 0

    while dq:
        dqSize = len(dq)

        count += 1
        for _ in range(dqSize):
            aP = dq.popleft()

            if aP == p2:
                return count - 1
            
            for rP in adjList[aP]:
                if not visit[rP]:
                    visit[rP] = True
                    dq.append(rP)
        
    return -1


n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

adjList = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)

for _ in range(m):
    p, s = map(int, input().split())

    adjList[p].append(s)
    adjList[s].append(p)

visit[p1] = True
print(BFS(p1))
