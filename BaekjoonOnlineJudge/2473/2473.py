from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

liquid = list(sorted(map(int, input().split())))

answer = 3000000001
answer_values = [0, 0, 0]

for base_index, value in enumerate(liquid):
    left = base_index + 1
    right = N - 1
    is_zero = False

    if left < right:
        window = deque()
        window.append(liquid[left])
        window.append(liquid[right])
        total = liquid[base_index] + liquid[left] + liquid[right]

    while left < right:
        if total == 0:
            is_zero = True
            answer_values[0] = liquid[base_index]
            answer_values[1] = liquid[left]
            answer_values[2] = liquid[right]
            break
        elif abs(total) < answer:
            answer = abs(total)
            answer_values[0] = liquid[base_index]
            answer_values[1] = liquid[left]
            answer_values[2] = liquid[right]

        if total < 0:
            window.popleft()
            total -= liquid[left]
            left += 1
            if left < right:
                window.append(liquid[left])
                total += liquid[left]
        else:
            window.pop()
            total -= liquid[right]
            right -= 1
            if left < right:
                window.append(liquid[right])
                total += liquid[right]

    if is_zero:
        break

print(*answer_values)
