import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    seq = list(map(int, input().split()))
    count = dict()

    c = 0
    for num in seq:
        if count.get(num, 0):
            continue
        else:
            count[num] = (c, num)
            c += 1
    
    for n in sorted((count.values())):
        print(n[1], end=" ")
