import sys
input = sys.stdin.readline

count = int(input())
electricWire = sorted([list(map(int,input().split())) for _ in range(count)])
memoization = [1 for _ in range(count)]

for i in range(1, count):
    for j in range(i):
        if electricWire[i][1] > electricWire[j][1]:
            memoization[i] = max(memoization[i], memoization[j]+1)

print(count - max(memoization))