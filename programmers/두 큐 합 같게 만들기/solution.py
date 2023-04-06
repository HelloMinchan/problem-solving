from collections import deque


def solution(queue1, queue2):
    answer = 0

    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    n = 600000

    for _ in range(n):
        if queue1_sum < queue2_sum:
            number = queue2.popleft()
            queue2_sum -= number
            queue1.append(number)
            queue1_sum += number
        elif queue1_sum > queue2_sum:
            number = queue1.popleft()
            queue1_sum -= number
            queue2.append(number)
            queue2_sum += number
        else:
            return answer

        answer += 1
    else:
        return -1
