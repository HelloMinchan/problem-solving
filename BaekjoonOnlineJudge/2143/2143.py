from collections import defaultdict
import sys

input = sys.stdin.readline

T = int(input())

n = int(input())
A = list(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))

b_sum_dict = defaultdict(int)

for i in range(m):
    tot = B[i]
    b_sum_dict[tot] += 1

    for j in range(i + 1, m):
        tot += B[j]
        b_sum_dict[tot] += 1

answer = 0
for left in range(n):
    tot = A[left]

    answer += b_sum_dict[T - tot]

    for right in range(left + 1, n):
        tot += A[right]
        answer += b_sum_dict[T - tot]

print(answer)
