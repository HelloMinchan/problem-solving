import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[1 << 30] * 200 for i in range(n + 1)]
dp[1][0] = 0
dic = {int(input()) for i in range(m)}

for i in range(2, n + 1):    
    if i in dic:
        continue
    for j in range(1, int(((i * 2) ** 0.5)) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1
    
result = min(dp[n])
print(-1 if result == (1 << 30) else result)
