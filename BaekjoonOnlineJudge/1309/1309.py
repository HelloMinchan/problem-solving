import sys

input = sys.stdin.readline

N = int(input())

dp_table = [[0,0,0] for _ in range(N+1)]

dp_table[1][0] = 1
dp_table[1][1] = 1
dp_table[1][2] = 1

for i in range(2, N+1):
    dp_table[i][0] = (dp_table[i-1][0] + dp_table[i-1][1] + dp_table[i-1][2]) % 9901
    dp_table[i][1] = (dp_table[i-1][0] + dp_table[i-1][2]) % 9901
    dp_table[i][2] = (dp_table[i-1][0] + dp_table[i-1][1]) % 9901

print(sum(dp_table[N]) % 9901)