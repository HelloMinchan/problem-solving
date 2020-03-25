import sys
input = sys.stdin.readline


def backTracking(index, N, S, sequence):
    global answer
    global visit
    global stack
    
    if len(stack) != 0 and sum(stack) == S:
        answer += 1

    for i in range(index, N):
        if not visit[i]:
            stack.append(sequence[i])
            visit[i] = True
            backTracking(i, N, S, sequence)
            stack.pop()
            visit[i] = False


N, S = map(int, input().split())
sequence = list(map(int, input().split()))
answer = 0
visit = [False] * N
stack = []

backTracking(0, N, S, sequence)
print(answer)