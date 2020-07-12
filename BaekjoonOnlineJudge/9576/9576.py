import sys
input = sys.stdin.readline


def biMatching(a):
    if visit[a]:
        return False

    visit[a] = True

    for b in adjList[a]:
        if B[b] == -1 or not visit[B[b]] and biMatching(B[b]):
            A[a] = b
            B[b] = a

            return True

    return False


MAX = 1001

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    adjList = [[] for _ in range(MAX)]

    A = [-1] * MAX
    B = [-1] * MAX

    for i in range(1, M + 1):
        a, b = map(int, input().split())

        for j in range(a, b + 1):
            adjList[i].append(j)

    match = 0

    for i in range(1, M + 1):
        visit = [False] * MAX
        if biMatching(i):
            match += 1

    print(match)
