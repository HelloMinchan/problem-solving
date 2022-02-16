import sys

input = sys.stdin.readline

N = int(input())
warehouse = [0] + list(map(int, input().split()))

dp_table = [0 for _ in range(N + 1)]
dp_table[1] = warehouse[1]
dp_table[2] = max(warehouse[1], warehouse[2])

for i in range(3, N + 1):
    dp_table[i] = max(dp_table[i - 1], warehouse[i] + dp_table[i - 2])

print(dp_table[-1])
