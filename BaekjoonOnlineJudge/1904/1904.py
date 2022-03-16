import sys

input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
    sys.exit(0)

dp_table = [0 for _ in range(N+1)]
dp_table[1] = 1
dp_table[2] = 2

for i in range(3, N+1):
    dp_table[i] = (dp_table[i-1] + dp_table[i-2]) % 15746

print(dp_table[-1])