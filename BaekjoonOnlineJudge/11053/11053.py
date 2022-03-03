import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp_table = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp_table[i] = max(dp_table[i], dp_table[j] + 1)

print(max(dp_table))
