import sys

input = sys.stdin.readline

M = int(input())

S = [0 for _ in range(21)]

for _ in range(M):
    command = input().split()
    operator = command[0]
    if operator not in ["all", "empty"]:
        number = int(command[1])

    if operator == "add":
        S[number] = 1
    elif operator == "remove":
        if S[number]:
            S[number] = 0
    elif operator == "check":
        print(S[number])
    elif operator == "toggle":
        S[number] = 0 if S[number] else 1
    elif operator == "all":
        S = [1 for _ in range(21)]
    else:
        S = [0 for _ in range(21)]
