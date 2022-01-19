import sys
input = sys.stdin.readline

def DFS(start_index):
    global answer

    if stack and sum(stack) == S:
        answer += 1        

    for index in range(start_index, len(sequence)):
        if not visit[index]:
            visit[index] = True
            stack.append(sequence[index])
            DFS(index + 1)
            visit[index] = False
            stack.pop()


N, S = map(int, input().split())
sequence = list(map(int, input().split()))
visit = [False for _ in range(len(sequence))]
stack = []

answer = 0

DFS(0)

print(answer)