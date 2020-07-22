import sys
input = sys.stdin.readline


def DFS(i, j, time):
    # 기저 사례
    if time > T:
        return 0
    if i == Xh and j == Yh:
        return 1

    if memoization[time][i][j] != -1:
        return memoization[time][i][j]
    
    memoization[time][i][j] = 0

    for way in range(4):
        ii = i + dx[way]
        jj = j + dy[way]

        if ii < 0 or ii > 410 or jj < 0 or jj > 410:
            continue

        if city[ii][jj]:
            continue
        
        memoization[time][i][j] = (memoization[time][i][j] + DFS(ii, jj, time + 1)) % 1000000007
    
    return memoization[time][i][j]


Xs, Ys = map(int, input().split())
T = int(input())
Xh, Yh = map(int, input().split())

# 좌표 변환
start_x = 210
start_y = 210
diff_x = start_x - Xs
diff_y = start_y - Ys
Xs = 210
Ys = 210
Xh += diff_x
Yh += diff_y

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
memoization = [[[-1] * 420 for _ in range(420)] for _ in range(203)]
city = [[0] * 420 for _ in range(420)]

N = int(input())
for _ in range(N):
    Xi, Yi = map(int, input().split())

    newXi = Xi + diff_x
    newYi = Yi + diff_y

    if newXi < 0 or newXi > 410 or newYi < 0 or newYi > 410:
        continue

    city[newXi][newYi] = 1

if Xh < 0 or Xh > 410 or Yh < 0 or Yh > 410:
    print(0)
    sys.exit(0)

print(DFS(210, 210, 0))
