import sys

input = sys.stdin.readline

N, M = map(int, input().split())
seq = list(map(int, input().split()))

answer = 0
start = 0
cur_sum = 0

for end, value in enumerate(seq):
    cur_sum += value

    if cur_sum >= M:
        if cur_sum == M:
            answer += 1
        else:
            while cur_sum >= M:
                cur_sum -= seq[start]
                start += 1

                if cur_sum == M:
                    answer += 1

print(answer)