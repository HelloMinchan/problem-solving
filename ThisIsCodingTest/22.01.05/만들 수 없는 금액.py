import sys
input = sys.stdin.readline

N = int(input())
coins = sorted(map(int, input().split()))
answer = 1

for coin in coins:
    if coin <= answer:
        answer += coin
    else:
        break

print(answer)
