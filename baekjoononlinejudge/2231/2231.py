import sys
input = sys.stdin.readline

N = int(input())

cons = N
for i in range(1, N):
    tot = 0
    for j in range(len(str(i))):
        tot += int(str(i)[j])
    if i + tot == N and cons > i:
        cons = i

if cons == N:
    print(0)
    exit()
    
print(cons)