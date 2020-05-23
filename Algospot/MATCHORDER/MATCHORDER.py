import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    member = int(input())
    russia = list(map(int, input().split()))
    korea = list(map(int, input().split()))
    win = 0

    russia.sort(reverse=True)
    korea.sort()

    for i in range(member):
        if russia[i] > korea[-1]:
            continue
        else:
            korea.pop()
            win += 1

    print(win)