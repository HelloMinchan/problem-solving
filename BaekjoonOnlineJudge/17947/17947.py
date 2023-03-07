import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

card = set(range(1, 4 * N + 1))

for _ in range(M):
    a, b = map(int, input().split())

    card.discard(a)
    card.discard(b)


chulyong = list(map(int, input().split()))
card.discard(chulyong[0])
card.discard(chulyong[1])

chulyong_score = abs(chulyong[0] % K - chulyong[1] % K)

card = list(card)
for i in range(len(card)):
    card[i] %= K
card.sort()

left = 0
right = len(card) // 2
answer = 0

while right < len(card) and answer < M - 1:
    if card[right] - card[left] > chulyong_score:
        answer += 1
        right += 1
        left += 1
    else:
        right += 1

print(answer)