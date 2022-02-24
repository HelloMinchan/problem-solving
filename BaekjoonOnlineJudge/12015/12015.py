# 4:47 ~ 4:54 (7분)

import sys, bisect

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

seq = [A[0]]

for i in range(1, N):
    if A[i] > seq[-1]:
        seq.append(A[i])
    else:
        new_i = bisect.bisect_left(seq, A[i])
        seq[new_i] = A[i]

print(len(seq))