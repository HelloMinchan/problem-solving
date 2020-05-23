import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    H, W, N = (map(int, input().split()))
    number = 1
    
    while N > H:
        N -= H
        number += 1
        
    print(str(N) + str(number) if number > 9 else str(N) + "0" + str(number))