import sys

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
    sys.exit(0)
elif n == 2:
    print(2)
    sys.exit(0)

dp_table = [0 for _ in range(n+1)]
dp_table[1] = 1
dp_table[2] = 2

for i in range(3, n+1):
    dp_table[i] = (dp_table[i-2] + dp_table[i-1]) % 10007

print(dp_table[-1])