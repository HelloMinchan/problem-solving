import sys
input = sys.stdin.readline


def recording(mid):
    count = 1
    length = 0

    for m in lessons:
        length += m
        if length > mid:
            length = m
            count += 1
    
    return count


N, M = map(int, input().split())
lessons = list(map(int, input().split()))

left = max(lessons)
right = sum(lessons)

while left <= right:
    mid = (left + right) // 2

    if M >= recording(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
