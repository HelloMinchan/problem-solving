import sys

input = sys.stdin.readline


def dfs(size, i, j):
    global answer
    
    if i == r and j == c:
        print(answer)
        sys.exit(0)

    if size == 1:
        answer += 1
        return

    if not (i <= r < i + size and j <= c < j + size):
        answer += size ** 2
        return

    new_size = size // 2
    
    dfs(new_size , i, j)

    dfs(new_size, i, j + new_size)

    dfs(new_size, i + new_size, j)

    dfs(new_size, i + new_size, j + new_size)


N, r, c = map(int, input().split())

answer = 0

dfs(2 ** N, 0, 0)