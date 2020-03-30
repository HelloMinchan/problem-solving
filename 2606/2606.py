from collections import deque
import sys
input = sys.stdin.readline


def BFS(dq):
    global visit, netWork

    while len(dq):
        virus = dq.popleft()

        if not visit[virus]:
            visit[virus] = True

            for netLine in netWork[virus]:
                if not visit[netLine]:
                    dq.append(netLine)


com = int(input())
visit = [False] * (com + 1)

netWorking = [tuple(map(int, input().split())) for _ in range(int(input()))]
netWork = [[0] for _ in range(com + 1)]
dq = deque()

for net in netWorking:
    netWork[net[0]].append(net[1])
    netWork[net[1]].append(net[0])

for netLine in netWork[1]:
    dq.append(netLine)

BFS(dq)

visit[0], visit[1] = False, False

print(visit.count(1))