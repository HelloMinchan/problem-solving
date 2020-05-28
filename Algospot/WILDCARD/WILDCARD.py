import sys
input = sys.stdin.readline


def isMatch(p1, p2):
    if memoization[p1][p2] != -1:
        return memoization[p1][p2]
    
    while p1 < len(W) and p2 < len(word) and (W[p1] == "?" or W[p1] == word[p2]):
        memoization[p1][p2] = isMatch(p1 + 1, p2 + 1)
        return memoization[p1][p2]
    
    if p1 == len(W):
        memoization[p1][p2] = (p2 == len(word))
        return memoization[p1][p2]

    if W[p1] == "*":
        if isMatch(p1 + 1, p2) or (p2 < len(word) and isMatch(p1, p2 + 1)):
            memoization[p1][p2] = 1
            return memoization[p1][p2]
    
    memoization[p1][p2] = 0
    return memoization[p1][p2]


C = int(input())

for _ in range(C):
    W = input().rstrip()
    N = int(input())
    words = sorted([input().rstrip() for _ in range(N)])
    memoization = [[-1] * 101 for _ in range(101)]
    
    for word in words:
        if isMatch(0, 0):
            print(word)