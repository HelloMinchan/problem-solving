import sys

input = sys.stdin.readline

N = int(input())

dp_table = [0 for _ in range(N+1)]

for num in range(2, N+1):
    dp_table[num] = dp_table[num-1] + 1

    if num % 2 == 0:
        dp_table[num] = min(dp_table[num], dp_table[num // 2] + 1)
    
    if num % 3 == 0:
        dp_table[num] = min(dp_table[num], dp_table[num // 3] + 1)

print(dp_table[-1])
