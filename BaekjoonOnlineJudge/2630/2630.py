import sys
input = sys.stdin.readline


def dfs(x, y, N):
    flag = False

    for i in range(x, x + N):
        if flag:
            break
        
        for j in range(y, y + N):
            if paper[x][y] != paper[i][j]:
                dfs(x, y, N // 2)
                dfs(x, y + N // 2, N // 2)
                dfs(x + N // 2, y, N // 2)
                dfs(x + N // 2, y + N // 2, N // 2)

                flag = True
                break
        
    if not flag:
        if paper[x][y] == 0:
            answer[0] += 1
        else:
            answer[1] += 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0]

dfs(0, 0, N)

for count in answer:
    print(count)