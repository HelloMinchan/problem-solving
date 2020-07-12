import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

while len(seq) != 1:
    n = len(seq)
    
    minX = 2147483647
    i = 0
    for j in range(n):
        if minX > seq[j]:
            minX = seq[j]
            i = j

    seq[i] = seq[i - 1]
    
    if i + 1 == n:
        seq[i] += seq[0]
    else:
        seq[i] += seq[i + 1]
        
    del seq[i - 1]
    
    if i == 0:
        del seq[i + 1]
    elif i == n - 1:
        del seq[0]
    else:
        del seq[i]

print(seq[0])
