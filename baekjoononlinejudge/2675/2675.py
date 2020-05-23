import sys
input = sys.stdin.readline

for _ in range(int(input())):
    case = list(input().rstrip().split())
    for i in range(len(case[1])):
        print(list(case[1])[i] * int(case[0]), end='')
    print()