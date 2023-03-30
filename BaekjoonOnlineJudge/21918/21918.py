import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lights = [0] + list(map(int, input().split()))

for _ in range(M):
    oper, a, b = map(int, input().split())

    if oper == 1:
        lights[a] = b
    elif oper == 2:
        for i in range(a, b + 1):
            if lights[i] == 0:
                lights[i] = 1
            else:
                lights[i] = 0
    elif oper == 3:
        for i in range(a, b + 1):
            lights[i] = 0
    else:
        for i in range(a, b + 1):
            lights[i] = 1

print(*lights[1:])
