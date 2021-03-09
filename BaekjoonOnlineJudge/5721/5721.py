import sys
input = sys.stdin.readline

while 1:
    M, N = map(int, input().split())

    if not M + N:
        break

    col = [0 for _ in range(M+1)]
    colMemoization = [0 for _ in range(M+1)]

    for i in range(1, M+1):
        row = [0] + list(map(int,input().split()))
        rowMemoization = [0 for _ in range(N+1)]

        for j in range(1, N+1):
            rowMemoization[j] = max(row[j], row[j-1])
            if j >= 2:
                rowMemoization[j] = max(row[j] + rowMemoization[j-2], rowMemoization[j-1])
        
        col[i] = rowMemoization[-1]
    
    for i in range(1, M+1):
        colMemoization[i] = max(col[i], col[i-1])
        if i >= 2:
            colMemoization[i] = max(col[i] + colMemoization[i-2], colMemoization[i-1])
    
    print(colMemoization[-1])