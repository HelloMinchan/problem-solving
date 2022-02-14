# 5:25 ~ 5:38 (13분)
import sys

input = sys.stdin.readline

board = input().rstrip()
answer = ""

i = 0
while i < len(board):
    if i + 3 < len(board) and board[i : i + 4] == "XXXX":
        answer += "AAAA"
        i += 4
    elif i + 1 < len(board) and board[i : i + 2] == "XX":
        answer += "BB"
        i += 2
    else:
        if board[i] == ".":
            while i < len(board) and board[i] == ".":
                answer += "."
                i += 1
        else:
            print(-1)
            break
else:
    print(answer)