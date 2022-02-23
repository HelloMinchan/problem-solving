# 11:24 ~ 11:33 (9분)
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coins = sorted([int(input()) for _ in range(N)], reverse=True)
answer = 0

now_money = K

for coin in coins:
    if coin <= now_money:
        answer += now_money // coin
        now_money %= coin

print(answer)
