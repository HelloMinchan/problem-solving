import sys
input = sys.stdin.readline

M, N = map(int, input().split())

check = [False for _ in range(N + 1)]
for i in range(2, N + 1):
    if check[i] == True:continue
    
    for j in range(i * i, N + 1, i):
        check[j] = True

for i in range(M, N + 1):
    if not check[i] and i != 1:
        print(i)