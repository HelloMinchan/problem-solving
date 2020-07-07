import sys
input = sys.stdin.readline


def DFS(s1, s2):
    if s1 >= len(X):
        return B * (len(Y) - s2)
    if s2 >= len(Y):
        return B * (len(X) - s1)

    if memoization[s1][s2] != -2147483647:
        return memoization[s1][s2]
    
    if X[s1] == Y[s2]:
        memoization[s1][s2] = max(memoization[s1][s2], A + DFS(s1 + 1, s2 + 1))
    else:
        memoization[s1][s2] = max(memoization[s1][s2], C + DFS(s1 + 1, s2 + 1))

    memoization[s1][s2] = max(memoization[s1][s2], B + DFS(s1 + 1, s2), B + DFS(s1, s2 + 1))
     
    return memoization[s1][s2]


A, B, C = map(int, input().split())
X = input().rstrip()
Y = input().rstrip()

memoization = [[-2147483647] * len(Y) for _ in range(len(X))]

print(DFS(0, 0))
