import sys
input = sys.stdin.readline


def dividend(target):
    tot = 0

    for req in require:
        if target >= req:
            tot += req
        else:
            tot += target
            
    return tot


N = int(input())
require = list(map(int, input().split()))
M = int(input())

left = 0
right = max(require)
answer = 0

while left <= right:
    mid = (left + right) // 2

    if dividend(mid) <= M:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
    
print(answer)
