for case in range(int(input())):
    N, k = map(int,  input().split())
    matrix =list(list(map(int, input().split())) for _ in range(N))
    t_matrix = list(zip(*matrix))
    place = 0
    for row in range(N):
        for i in range(N-k+1):
            if sum(matrix[row][i:i+k]) == k:
                if i == 0:
                    if matrix[row][i+k] == 0:
                        place += 1
                elif i == N-k:
                    if matrix[row][i-1] == 0:
                        place += 1
                else:
                    if matrix[row][i+k] == 0 and matrix[row][i-1] == 0:
                        place += 1
        for i in range(N-k+1):
            if sum(t_matrix[row][i:i+k]) == k:
                if i == 0:
                    if t_matrix[row][i+k] == 0:
                        place += 1
                elif i == N-k:
                    if t_matrix[row][i-1] == 0:
                        place += 1
                else:
                    if t_matrix[row][i+k] == 0 and t_matrix[row][i-1] == 0:
                        place += 1

    print(f'#{case+1} {place}')
