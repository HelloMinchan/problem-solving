from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bridges = [list(map(int, input().split())) for _ in range(M)]
factory = list(map(int, input().split()))
result = 0

adjacentList = [[] for _ in range(N + 1)]

for bridge in bridges:
    adjacentList[bridge[0]].append((bridge[1], bridge[2]))
    adjacentList[bridge[1]].append((bridge[0], bridge[2]))


def BFS(vertex, mid):
    visit = [False] * (N + 1)
    dq = deque()

    dq.append(vertex)

    while len(dq):
        vertex = dq.popleft()

        if not visit[vertex]:
            visit[vertex] = True
            
            if vertex == factory[1]:
                return True

            for edge in adjacentList[vertex]:
                if edge[1] >= mid:
                    dq.append(edge[0])

    return False


left = 0
right = 1000000000

while left <= right:
    mid = (left + right) // 2

    if BFS(factory[0], mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)