import sys, heapq

input = sys.stdin.readline

N = int(input())
sequence = [int(input()) for _ in range(N)]
answer = 0

negative_numbers = []
positive_numbers = []

for number in sequence:
    if number <= 0:
        heapq.heappush(negative_numbers, number)
    else:
        heapq.heappush(positive_numbers, -number)

while negative_numbers:
    a = heapq.heappop(negative_numbers)

    if negative_numbers:
        b = heapq.heappop(negative_numbers)

        answer += a * b
    else:
        answer += a

while positive_numbers:
    a = -heapq.heappop(positive_numbers)

    if a == 1:
        answer += a
    else:
        if positive_numbers:
            b = -heapq.heappop(positive_numbers)

            if b == 1:
                answer += a + b
            else:
                answer += a * b
        else:
            answer += a

print(answer)
