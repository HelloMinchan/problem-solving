import sys

input = sys.stdin.readline

N, K = map(int, input().split())

memoization = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
knapsack = [(0, 0)]

for _ in range(N):
    knapsack.append(tuple(map(int, input().split())))

for stuffCount in range(1, N + 1):
    for possibleWeight in range(1, K + 1):
        if possibleWeight < knapsack[stuffCount][0]:
            memoization[stuffCount][possibleWeight] = memoization[stuffCount - 1][
                possibleWeight
            ]
        else:
            memoization[stuffCount][possibleWeight] = max(
                memoization[stuffCount - 1][possibleWeight],
                memoization[stuffCount - 1][possibleWeight - knapsack[stuffCount][0]]
                + knapsack[stuffCount][1],
            )

print(memoization[N][K])
