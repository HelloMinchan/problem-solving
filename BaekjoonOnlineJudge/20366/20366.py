import sys

input = sys.stdin.readline

N = int(input())
length = list(sorted(map(int, input().split())))

answer = sys.maxsize

for elsa_left in range(N):
    for elsa_right in range(elsa_left + 3, N):
        elsa_snowman_length = length[elsa_left] + length[elsa_right]
        anna_left = elsa_left + 1
        anna_right = elsa_right - 1

        while anna_left < anna_right:
            anna_snowman_length = length[anna_left] + length[anna_right]

            length_diff = elsa_snowman_length - anna_snowman_length

            if abs(length_diff) < answer:
                answer = abs(length_diff)

            if length_diff > 0:
                anna_left += 1
            else:
                anna_right -= 1

print(answer)
