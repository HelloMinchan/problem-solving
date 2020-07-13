import sys
input = sys.stdin.readline

N, K = map(int, input().split())

seq = list(range(1, N + 1))
answer = []
cur = 0

while seq:
    cur = (cur + K - 1) % len(seq)
    answer.append(str(seq[cur]))
    del seq[cur]

print('<', ", ".join(answer), '>', sep="")
