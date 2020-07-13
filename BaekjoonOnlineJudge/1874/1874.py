import sys
input = sys.stdin.readline

n = int(input())
seq = [int(input()) for _ in range(n)]
stack = []
answer = []

cur = 0
for i in range(1, n + 1):
    stack.append(i)
    answer.append('+')
    
    while cur < n and stack and stack[-1] == seq[cur]:
        stack.pop()
        answer.append('-')
        cur += 1

if stack:
    print("NO")
else:
    print("\n".join(answer))
