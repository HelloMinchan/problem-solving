import sys

input = sys.stdin.readline

def dfs(a, b, c):
    if dp_table[a][b][c] != INF:
        return dp_table[a][b][c]

    if a <= 0 or b <= 0 or c <= 0:
        dp_table[a][b][c] = 1
        return 1
    if a > 20 or b > 20 or c > 20:
        dp_table[a][b][c] = dfs(20, 20, 20)
        return dp_table[a][b][c]
    if a < b and b < c:
        dp_table[a][b][c] = dfs(a, b, c-1) + dfs(a, b-1, c-1) - dfs(a, b-1, c)
        return dp_table[a][b][c]
    
    dp_table[a][b][c] = dfs(a-1, b, c) + dfs(a-1, b-1, c) + dfs(a-1, b, c-1) - dfs(a-1, b-1, c-1)
    
    return dp_table[a][b][c]

INF = 2147483647
dp_table = [[[INF for _ in range(101)] for _ in range(101)] for _ in range(101)]

while 1:
    a, b, c = map(int,input().split())

    if a == -1 and b == -1 and c == -1:
        break

    print(f"w({a}, {b}, {c}) = {dfs(a, b, c)}")