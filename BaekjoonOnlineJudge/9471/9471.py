import sys
input = sys.stdin.readline


def pisano():
    back2 = 0
    back1 = 0
    now = 1
    count = 0

    while 1:
        back2 = back1
        back1 = now
        now = (back1 + back2) % M
        count += 1

        if back1 == 0 and now == 1:
            return count


P = int(input())

for _ in range(P):
    N, M = map(int, input().split())

    print(N, pisano())
