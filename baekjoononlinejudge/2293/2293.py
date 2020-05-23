import sys
input = sys.stdin.readline

n, k = map(int, input().split())
values = [int(input()) for _ in range(n)]
memoization = [1] + [0] * k

for i in range(n):    
    for j in range(1, k + 1):
        if j - values[i] >= 0:
            memoization[j] += memoization[j - values[i]]

print(memoization[-1])