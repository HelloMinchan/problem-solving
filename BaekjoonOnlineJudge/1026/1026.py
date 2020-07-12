import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

answer = 0

for i in range(N):
    answer += A[i] * B[i]

print(answer)
