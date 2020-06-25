import sys
input = sys.stdin.readline


def TSP(sv, visited):
    if memoization[sv][visited]:
        return memoization[sv][visited]
    
    if visited == ((1 << N) - 1):
        if adjMatrix[sv][0]:
            return adjMatrix[sv][0]
        return 2147483647
    
    memoization[sv][visited] = 2147483647

    for i in range(N):
        if visited & (1 << i) or not adjMatrix[sv][i]:
            continue

        memoization[sv][visited] = min(memoization[sv][visited], TSP(i, visited | (1 << i)) + adjMatrix[sv][i])
        
    return memoization[sv][visited]


N = int(input())
adjMatrix = [list(map(int, input().split())) for _ in range(N)]
memoization = [[0] * (1 << N) for _ in range(N)]

print(TSP(0, 1))
