import sys
input = sys.stdin.readline


def binary(n, m):
    if memoization[n][m] != -1:
        return memoization[n][m]
    if n == 0 or m == 0:
        memoization[n][m] = 1
        return memoization[n][m]
    
    memoization[n][m] = binary(n - 1, m)

    if m > 0:
        memoization[n][m] += binary(n - 1, m - 1)

    return memoization[n][m]


def makeBinary(n, m, nth):
    global answer

    if n == 0:
        return
    if m == 0:
        for _ in range(n):
            answer += '0'
        return
    
    pivot = binary(n - 1, m)
    if nth <= pivot:
        answer += '0'
        makeBinary(n - 1, m, nth)
    else:
        answer += '1'
        makeBinary(n - 1, m - 1, nth - pivot)


N, L, I = map(int, input().split())

memoization = [[-1] * (L + 1) for _ in range(N + 1)]

answer = ""
makeBinary(N, L, I)

print(answer)
