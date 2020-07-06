import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    
    isAllZero = True
    isPossible = True
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                isAllZero = False
                neighbor = 0

                for way in range(4):
                    ii = i + dx[way]
                    jj = j + dy[way]

                    if ii < 0 or ii > n - 1 or jj < 0 or jj > m - 1:
                        continue

                    neighbor += 1

                if grid[i][j] > neighbor:
                    isPossible = False
                    break
            
        if not isPossible:
            break
    
    if not isPossible:
        print("NO")
    else:
        print("YES")
        if isAllZero:
            for line in grid:
                print(*line)
        else:
            for i in range(n):
                for j in range(m):
                    if i == 0 or i == n - 1:
                        if j == 0 or j == m - 1:
                            print(2, end=" ")
                        else:
                            print(3, end=" ")
                    else:
                        if j == 0 or j == m - 1:
                            print(3, end=" ")
                        else:
                            print(4, end=" ")
                print()
