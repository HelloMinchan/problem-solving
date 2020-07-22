import sys
input = sys.stdin.readline


def DFS(i, j, di, distance):
    if i < 1 or i > N or j < 1 or j > M:
        return [0, 0]

    if memoization[di][i][j][0] != -1:
        return memoization[di][i][j]

    memoization[di][i][j] = [0, 0]
    memoization[di][i][j] = [0, 0]

    if room[i][j] == '!':
        ii = i + directrion[di][0]
        jj = j + directrion[di][1]
        
        temp = DFS(ii, jj, di, distance + 1)
        
        memoization[di][i][j][0] += temp[0] + 1
        memoization[di][i][j][1] += temp[1] + distance
    else:
        # 거울 일경우
        if room[i][j] == '/':
            if order[0] == 'L':
                ii = i + directrion[3][0]
                jj = j + directrion[3][1]
                temp = DFS(ii, jj, 3, distance + 1)
            elif order[0] == 'R':
                ii = i + directrion[2][0]
                jj = j + directrion[2][1]
                temp = DFS(ii, jj, 2, distance + 1)
            elif order[0] == 'U':
                ii = i + directrion[1][0]
                jj = j + directrion[1][1]
                temp = DFS(ii, jj, 1, distance + 1)
            else:
                ii = i + directrion[0][0]
                jj = j + directrion[0][1]
                temp = DFS(ii, jj, 0, distance + 1)
        elif room[i][j] == '\\':
            if order[0] == 'L':
                ii = i + directrion[2][0]
                jj = j + directrion[2][1]
                temp = DFS(ii, jj, 2, distance + 1)
            elif order[0] == 'R':
                ii = i + directrion[3][0]
                jj = j + directrion[3][1]
                temp = DFS(ii, jj, 3, distance + 1)
            elif order[0] == 'U':
                ii = i + directrion[0][0]
                jj = j + directrion[0][1]
                temp = DFS(ii, jj, 0, distance + 1)
            else:
                ii = i + directrion[1][0]
                jj = j + directrion[1][1]
                temp = DFS(ii, jj, 1, distance + 1)
        # 빈 공간
        else:
            ii = i + directrion[di][0]
            jj = j + directrion[di][1]
            temp = DFS(ii, jj, di, distance + 1)

        memoization[di][i][j][0] += temp[0]
        memoization[di][i][j][1] += temp[1]
    
    return memoization[di][i][j]


N, M, K, Q = map(int, input().split())

room = [[0] * (M + 1) for _ in range(N + 1)]
memoization = [[[[-1, -1] for _ in range(M + 1)] for _ in range(N + 1)] for _ in range(4)]

# L(0), R(1), U(2), D(3) 
directrion = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(K):
    x, y, stuff = tuple(input().split())

    room[int(x)][int(y)] = stuff

for _ in range(Q):
    answer = 0
    order = input().rstrip()

    if order[0] == 'L':
        answer = DFS(int(order[1]), 1, 0, 1)
    elif order[0] == 'R':
        answer = DFS(int(order[1]), M, 1, 1)
    elif order[0] == 'U':
        answer = DFS(1, int(order[1]), 2, 1)
    else:
        answer = DFS(N, int(order[1]), 3, 1)

    print(*answer)
