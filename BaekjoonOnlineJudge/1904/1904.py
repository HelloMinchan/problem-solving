import sys

input = sys.stdin.readline

N = int(input())

dp_table = [0 for _ in range(N+1)]

for i in range(1, N+1):
    if i == 1:
        dp_table[i] = 1
    elif i == 2:
        dp_table[i] = 2
    else:
        dp_table[i] = (dp_table[i-1] + dp_table[i-2]) % 15746

print(dp_table[-1])
