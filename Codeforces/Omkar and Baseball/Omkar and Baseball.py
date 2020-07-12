import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    sequence = list(map(int, input().split()))
    temp = sorted(sequence)
    
    answer = 0
    isDiff = True
    for i in range(n):
        if sequence[i] != temp[i] and isDiff:
            isDiff = False
            answer += 1
        elif sequence[i] == temp[i]:
            isDiff = True

    print(answer)
