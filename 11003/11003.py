import sys
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))
window = []
for i in range(N):
    if i < L:
        window.append(A[i])
        print(min(window), end=" ")
        continue
    window.append(A[i])
    del window[0]
    print(min(window), end=" ")