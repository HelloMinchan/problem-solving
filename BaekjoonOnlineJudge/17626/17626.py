import sys, math

input = sys.stdin.readline


n = int(input())

dp_table = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    if i == 1:
        dp_table[1] = 1
    else:
        dp_table[i] = 2147483647

        for j in range(1, int(math.sqrt(i)) + 1):
            dp_table[i] = min(dp_table[i], dp_table[i - j ** 2] + 1)


print(dp_table[n])