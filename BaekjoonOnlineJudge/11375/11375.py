import sys
input = sys.stdin.readline

MAX = 1001


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


N, M = map(int, input().split())

adjList = [[] for _ in range(MAX)]

groupA = [-1] * MAX
groupB = [-1] * MAX
answer = 0

for i in range(1, N + 1):
    temp = list(map(int, input().split()))

    for j in temp[1:]:
        adjList[i].append(j)

for i in range(1, N + 1):
    visit = [False] * MAX
    if biMatching(i):
        answer += 1

print(answer)
