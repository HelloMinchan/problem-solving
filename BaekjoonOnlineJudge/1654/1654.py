import sys
input = sys.stdin.readline


def cutRAN(mid):
    count = 0

    for length in RAN:
        count += length // mid
    
    return count
        

K, N = map(int, input().split())
RAN = [int(input()) for _ in range(K)]

left = 1
right = max(RAN)
answer = 0

while left <= right:
    mid = (left + right) // 2

    if cutRAN(mid) >= N:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
