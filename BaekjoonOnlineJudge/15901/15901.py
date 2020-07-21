from collections import deque
import sys
input = sys.stdin.readline

N, M, K, Q = map(int, input().split())
seq = list(map(int, input().split()))
incinerator = [0] * 500001

for _ in range(Q):
    order = list(map(int, input().split()))

    if order[0]:

    elif order[0]:

    elif order[0]:
        
    else:
