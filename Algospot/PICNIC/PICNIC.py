import sys
input = sys.stdin.readline


def DFS(startI, remainingFriend):
    if not remainingFriend:
        return 1

    possibleCase = 0

    for i in range(startI, n):
        if not visit[i]:
            for j in range(i + 1, n):
                if not visit[j] and isFriend[i][j]:
                    visit[i] = visit[j] = True
                    possibleCase += DFS(i, remainingFriend - 2)
                    visit[i] = visit[j] = False
    
    return possibleCase


C = int(input())

for _ in range(C):
    n, m = map(int, input().split())
    visit = [False] * n
    isFriend = [[False] * n for _ in range(n)]
    friendsList = list(map(int, input().split()))

    for i in range(0, len(friendsList), 2):
        isFriend[friendsList[i]][friendsList[i + 1]] = True
        isFriend[friendsList[i + 1]][friendsList[i]] = True

    print(DFS(0, n))