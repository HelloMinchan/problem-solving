import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans1 = 0
ans2 = 0

for i in range(N):
    ans1 += (A[i] & B[i])
    ans2 &= (A[i] + B[i])
    
print(ans1, ans2)
