import sys
input = sys.stdin.readline


def biMatching(worker):
    if visit[worker]:
        return False
    
    visit[worker] = True

    for work in adjList[worker]:
        if groupB[work] == -1 or not visit[groupB[work]] and biMatching(groupB[work]):
            groupA[worker] = work
            groupB[work] = worker

            return True
    
    return False


MAX = 1001

N, M, K = map(int, input().split())

adjList = [[] for _ in range(MAX)]

for i in range(1, N + 1):
    temp = list(map(int, input().split()))

    for j in temp[1:]:
        adjList[i].append(j)

groupA = [-1 for _ in range(MAX)]
groupB = [-1 for _ in range(MAX)]

answer = 0

for i in range(1, N + 1):
    visit = [False] * MAX
    if biMatching(i):
        answer += 1

hardWorker = 0
for i in range(1, N + 1):
    visit = [False] * MAX
    if biMatching(i):
        answer += 1
        hardWorker += 1

        if hardWorker == K:
            break

print(answer)
