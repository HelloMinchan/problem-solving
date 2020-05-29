import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    N, K = map(int, input().split())
    soldiers = [i + 1 for i in range(N)]

    i = 0
    while len(soldiers) != 2:
        del soldiers[i]
        i += K - 1
        i %= len(soldiers)
    
    print(*soldiers)