import sys
input = sys.stdin.readline

N, C = map(int, input().split())
w = list(map(int, input().split()))
seq = list(map(int, input().split()))

answer = []
i = N - 1
j = N - 1
while 1:
    if w[i] != seq[j]:
        i -= 1
    elif i != j:
        answer.append(i + 1, j + 1)
