# 3:46 ~ 3:51 (5분)

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
seq = list(map(int, input().split()))

end = 0
length = 0
answer = 0
count = 0

for start in range(N):
    while count <= K and end < N:
        if seq[end] % 2 == 1:
            count += 1
        else:
            length += 1
        end += 1

    answer = max(answer, length)

    if seq[start] % 2 == 1:
        count -= 1
    else:
        length -= 1

print(answer)