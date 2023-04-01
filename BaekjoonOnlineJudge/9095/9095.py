import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def dfs(number):
    if number < 0:
        return 0
    if number == 1:
        memoization[number] = 1
        return memoization[number]
    if number == 2:
        memoization[number] = 2
        return memoization[number]
    if number == 3:
        memoization[number] = 4
        return memoization[number]

    if memoization[number] != -1:
        return memoization[number]

    memoization[number] = 0
    memoization[number] = dfs(number - 1) + dfs(number - 2) + dfs(number - 3)

    return memoization[number]


T = int(input())
memoization = [-1 for _ in range(11)]

while T:
    T -= 1

    n = int(input())

    print(dfs(n))
