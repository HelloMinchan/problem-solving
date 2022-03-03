import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    results = input().rstrip()
    answer = 0
    score_stack = 0

    for result in results:
        if result == "O":
            score_stack += 1
            answer += score_stack
        else:
            score_stack = 0
        
    print(answer)