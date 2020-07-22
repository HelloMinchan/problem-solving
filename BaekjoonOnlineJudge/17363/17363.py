import sys
input = sys.stdin.readline

N, M = map(int, (input().split()))

picture = [reversed(list(input().rstrip())) for _ in range(N)]

for line in zip(*picture):
    for s in line:
        if s == '-':
            print('|', end="")
        elif s == '|':
            print('-', end="")
        elif s == '/':
            print('\\', end="")
        elif s == '\\':
            print('/', end="")
        elif s == '^':
            print('<', end="")
        elif s == '<':
            print('v', end="")
        elif s == 'v':
            print('>', end="")
        elif s == '>':
            print('^', end="")
        else:
            print(s, end="")
    print()
    
