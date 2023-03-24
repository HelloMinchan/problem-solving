import sys

input = sys.stdin.readline

N = int(input())
liquids = list(sorted(map(int, input().split())))

answer = sys.maxsize
answer_left = 0
answer_right = 0
left = 0
right = N - 1

while left < right:
    tot = liquids[left] + liquids[right]

    if tot > 0:
        if answer > tot:
            answer = tot
            answer_left = liquids[left]
            answer_right = liquids[right]

        right -= 1
    else:
        if answer > abs(tot):
            answer = abs(tot)
            answer_left = liquids[left]
            answer_right = liquids[right]

        left += 1

print(answer_left, answer_right)
