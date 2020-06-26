import sys
input = sys.stdin.readline


def pisano(M):
    back2 = 0
    back1 = 1
    now = 0
    count = 0

    while 1:
        now = back1 + back2 % M

        back1 = back2
        back2 = now

        count += 1
        
        if back1 == 0 and back2 == 1:
            return count


P = int(input())

for _ in range(P):
    N, M = map(int, input().split())

    print(N, pisano(M))
