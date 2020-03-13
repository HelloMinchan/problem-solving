import sys
input = sys.stdin.readline

ck = [ False, False ] + [ True ] * (10000 - 1)
for i in range(2, 10001):
    if ck[i] == False : continue
    for j in range(i * 2, 10001, i):
        ck[j] = False

for _ in range(int(input())):
    target = int(input())
    halfTarget = target // 2
    for i in range(halfTarget, 1, -1):
        if (ck[i] and ck[target - i]):
            print(f"{i} {target - i}")
            break