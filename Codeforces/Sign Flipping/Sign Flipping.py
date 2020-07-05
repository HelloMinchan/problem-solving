import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    n = int(input())
    seq = list(map(int, input().split()))

    for i in range(n):
        if i % 2:
            if seq[i] < 0:
                seq[i] = -seq[i]
        else:
            if -seq[i] < 0:
                seq[i] = -seq[i]
    
    print(*seq)

