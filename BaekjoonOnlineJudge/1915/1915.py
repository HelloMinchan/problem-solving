import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
dx, dy = [-1, 0, -1], [0, -1, -1]
maxLength = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == '1':
            length = []

            for way in range(3):
                ii = i + dx[way]
                jj = j + dy[way]

                if ii < 0 or ii > n - 1 or jj < 0 or jj > m - 1:
                    continue

                if arr[ii][jj] and arr[ii][jj] != '0':
                    length.append(int(arr[ii][jj]))
            
            countLength = len(length)
            if countLength:
                minLength = min(length)
            else:
                minLength = 0

            if countLength == 3:
                arr[i][j] = minLength + 1
            else:
                arr[i][j] = int(arr[i][j])

            if maxLength < arr[i][j]:
                maxLength = arr[i][j]

print(maxLength ** 2)