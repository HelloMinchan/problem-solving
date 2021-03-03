import sys
input = sys.stdin.readline

def DFS(W, H):
    if not W:
        return 1
    if memoization[W][H]:
        return memoization[W][H]
    
    memoization[W][H] = DFS(W-1, H+1)

    if H > 0:
        memoization[W][H] += DFS(W, H-1)
    
    return memoization[W][H]


memoization = [[0 for _ in range(31)] for _ in range(31)]

while 1:
    N = int(input())

    if not N:
        break

    print(DFS(N, 0))