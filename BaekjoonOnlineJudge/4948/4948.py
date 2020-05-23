import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    check = [False for _ in range(2 * n + 1)]
    for i in range(2, 2 * n):
        if check[i] == True:continue
        
        for j in range(i * i, 2 * n + 1, i):
            check[j] = True

    count = 0
    for i in range(n + 1, 2 * n + 1):
        if not check[i] and i != 1:
            count += 1
    
    print(count)