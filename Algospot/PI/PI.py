import sys
input = sys.stdin.readline


def diffCheck3(n1, n2, n3):
    if n1 == n2 == n3:
        return 1
    if n1 - n2 == n2 - n3 and abs(n1 - n2) == 1:
        return 2
    if n1 == n2 != n3:
        return 4
    if n1 - n2 == n2 - n3:
        return 5
    return 10


def diffCheck4(n1, n2, n3, n4):
    if n1 == n2 == n3 == n4:
        return 1
    if n1 - n2 == n2 - n3 == n3 - n4 and abs(n1 - n2) == 1:
        return 2
    if n1 == n3 and n2 == n4:
        return 4
    if n1 - n2 == n2 - n3 == n3 - n4:
        return 5
    return 10


def diffCheck5(n1, n2, n3, n4, n5):
    if n1 == n2 == n3 == n4 == n5:
        return 1
    if n1 - n2 == n2 - n3 == n3 - n4 == n4 - n5 and abs(n1 - n2) == 1:
        return 2
    if n1 == n3 == n5 and n2 == n4:
        return 4
    if n1 - n2 == n2 - n3 == n3 - n4 == n4 - n5:
        return 5
    return 10


C = int(input())

for _ in range(C):
    partition = list(map(int, input().rstrip()))
    memoization = [0] * len(partition)

    memoization[2] = diffCheck3(partition[2], partition[1], partition[0])
    memoization[3] = diffCheck4(partition[3], partition[2], partition[1], partition[0])
    memoization[4] = diffCheck5(partition[4], partition[3], partition[2], partition[1], partition[0])

    for i in range(5, len(partition)):
        minDiff = []
        if memoization[i - 3]:
            minDiff.append(memoization[i - 3] + diffCheck3(partition[i - 2], partition[i - 1], partition[i]))
        if memoization[i - 4]:
            minDiff.append(memoization[i - 4] + diffCheck4(partition[i - 3], partition[i - 2], partition[i - 1], partition[i]))
        if memoization[i - 5]:
            minDiff.append(memoization[i - 5] + diffCheck5(partition[i - 4], partition[i - 3], partition[i - 2], partition[i - 1], partition[i]))
        
        memoization[i] = min(minDiff)
    
    print(memoization[-1])