from collections import deque
import sys, copy
input = sys.stdin.readline


def findCrash(groupNum, x, y, target):
    dq = deque()
    dq.append((x, y))

    count = 0
    while dq:
        i, j = dq.popleft()
        count += 1

        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > 5 or jj < 0 or jj > 11:
                continue

            if board[ii][jj] == target and not visit[ii][jj]:
                visit[ii][jj] = groupNum
                dq.append(((ii, jj)))
        
    if count >= 4:
        return True

    return False


def boardRebuild():
    global board

    for i in range(6):
        crashNum = deque(visit[i])
        boardState = deque(board[i])

        index = 0

        while crashNum:
            num = crashNum.popleft()

            if num not in willCrash:
                board[i][index] = boardState.popleft()
                index += 1
            else:
                boardState.popleft()
            
        while index != 12:
            board[i][index] = '.'
            index += 1


board = [list(input().rstrip()) for _ in range(12)]

# 게임판의 끝을 왼쪽으로 변경
board = [list(reversed(x)) for x in zip(*board)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
score = 0

while 1:
    willCrash = []
    visit = [[0] * 12 for _ in range(6)]

    groupNum = 1
    for i in range(6):
        for j in range(12):
            if board[i][j] != '.' and not visit[i][j]:
                visit[i][j] = groupNum
                if findCrash(groupNum, i, j, board[i][j]):
                    willCrash.append(groupNum)
                groupNum += 1

    if not willCrash:
        print(score)
        break
    else:
        score += 1
        boardRebuild()
