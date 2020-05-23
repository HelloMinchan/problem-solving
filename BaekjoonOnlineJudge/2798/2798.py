import sys
input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))

tot = 0
for i in range(0, N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if tot < card[i] + card[j] + card[k] and card[i] + card[j] + card[k] <= M:
                tot = card[i] + card[j] + card[k]

print(tot)