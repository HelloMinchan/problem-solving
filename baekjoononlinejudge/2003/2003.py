import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

sP = eP = tot = 0
ans = 0

while(True):
    if tot >= M:
        tot -= A[eP]
        eP += 1
    elif sP == len(A):
        break
    else:
        tot += A[sP]
        sP += 1
    
    if tot == M:
        ans += 1

print(ans)