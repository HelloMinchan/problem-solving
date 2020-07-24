import sys, copy
input = sys.stdin.readline


def pCheck(x, L):
    if not stack:
        return True
    
    if p[L - 1] == '<':
        if stack[-1] < x:
            return True
        return False
    else:
        if stack[-1] > x:
            return True
        return False


def DFS(L):
    if L == k + 1:
        answer.append(copy.deepcopy(stack))
        return

    for i in range(10):
        if not visit[i]:
            if pCheck(i, L):
                visit[i] = True
                stack.append(i)
                DFS(L + 1)
                visit[i] = False
                stack.pop()


k = int(input())
p = list(input().rstrip().split())

visit = [False] * 10
answer = []
stack = []

DFS(0)

print(*answer[-1], sep="")
print(*answer[0], sep="")
