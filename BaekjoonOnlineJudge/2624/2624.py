# Python3 TLE
# PyPy3 AC

import sys
input = sys.stdin.readline

T = int(input())
k = int(input())

memoization = [0 for _ in range(T+1)]
memoization[0] = 1

coins = []
for _ in range(k):
    price, count = map(int ,input().split())
    coins.append((price, count))

coins.sort()

for i in range(k):
    for j in range(T, -1, -1):
        for k in range(1, coins[i][1]+1):
            if j - coins[i][0] * k >= 0:
                memoization[j] += memoization[j - coins[i][0] * k]
    
print(memoization[-1])