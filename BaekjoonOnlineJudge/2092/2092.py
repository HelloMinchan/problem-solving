import sys
input = sys.stdin.readline

T, A, S, B = map(int, input().split())
nums = list(map(int, input().split()))

table = [0] * 201

for n in nums:
    table[n] += 1

memoization = [[0] * (A + 1) for _ in range(201)]
memoization[0][0] = 1

for i in range(1, T + 1):
    for k in range(table[i] + 1):
        memoization[i][k] += 1
    
    for j in range(1, A + 1):
        memoization[i][j] += memoization[i - 1][j]

        for k in range(1, table[i] + 1):
            if j - k > 0:
                memoization[i][j] += memoization[i - 1][j - k]
                memoization[i][j] %= 1000000
    
answer = 0
for i in range(S, B + 1):
    answer += memoization[T][i] % 1000000

print(answer % 1000000)
