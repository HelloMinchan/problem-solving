import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def DFS(root):
    visit[root] = True
    memoization[root] = 1

    for childNode in tree[root]:
        if not visit[childNode]:
            DFS(childNode)
            memoization[root] += memoization[childNode]

    return

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
memoization = [0 for _ in range(N+1)]
visit = [False for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, input().split())

    tree[U].append(V)
    tree[V].append(U)

DFS(R)

for _ in range(Q):
    query = int(input())
    print(memoization[query])