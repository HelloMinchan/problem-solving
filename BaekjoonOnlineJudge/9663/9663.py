def DFS(row):
    global answer
    
    if row == N:
        answer += 1
    
    for col in range(N):
        if not col_check[col] and not back_slash_direction_check[col + row] and not slash_direction_check[col - row + N - 1]:
            col_check[col] = True
            back_slash_direction_check[col + row] = True
            slash_direction_check[col - row + N - 1] = True
            DFS(row + 1)
            col_check[col] = False
            back_slash_direction_check[col + row] = False
            slash_direction_check[col - row + N - 1] = False


N = int(input())

col_check = [False for _ in range(N)]
slash_direction_check = [False for _ in range(N * 2 - 1)]
back_slash_direction_check = [False for _ in range(N * 2 - 1)]
answer = 0

DFS(0)

print(answer)