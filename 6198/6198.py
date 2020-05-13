import sys
input = sys.stdin.readline

N = int(input())
h = [int(input()) for _ in range(N)]
stack = []
ans = 0

for i in range(N - 1, -1, -1):
    seeable = 0
    while(True):
        if not len(stack):
            stack.append((0, h[i]))
            break

        if stack[-1][1] < h[i]:
            seeable += stack.pop()[0] + 1

            while(True):
                if not len(stack):
                    stack.append((seeable, h[i]))
                    ans += seeable
                    break
                if stack[-1][1] < h[i]:
                    seeable += stack.pop()[0] + 1
                else:
                    stack.append((seeable, h[i]))
                    ans += seeable
                    break

            break
        else:
            stack.append((0, h[i]))
            break

print(ans)