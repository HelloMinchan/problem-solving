import sys, itertools

input = sys.stdin.readline


def win_by_3_check(board, is_full, x_count, o_count):
    x_win_count = 0
    o_win_count = 0

    for row in board:
        if row.count("X") == 3:
            x_win_count += 1
        elif row.count("O") == 3:
            o_win_count += 1

    for col in zip(*board):
        if col.count("X") == 3:
            x_win_count += 1
        elif col.count("O") == 3:
            o_win_count += 1

    if [board[0][0], board[1][1], board[2][2]].count("X") == 3:
        x_win_count += 1
    if [board[0][0], board[1][1], board[2][2]].count("O") == 3:
        o_win_count += 1
    if [board[0][2], board[1][1], board[2][0]].count("X") == 3:
        x_win_count += 1
    if [board[0][2], board[1][1], board[2][0]].count("O") == 3:
        o_win_count += 1

    # 꽉채움
    if is_full:
        # X가 이긴 경우
        if x_win_count >= 1 and o_win_count == 0:
            return True
        # 무승부인 경우
        elif x_win_count == 0 and o_win_count == 0:
            return True
    # 빔
    else:
        # X가 이긴 경우
        if x_win_count == 1 and o_win_count == 0 and x_count == o_count + 1:
            return True
        # O가 이긴 경우
        elif x_win_count == 0 and o_win_count == 1 and x_count == o_count:
            return True

    return False


while True:
    input_string = input().rstrip()
    if input_string == "end":
        break

    board = []
    board.append(list(input_string[:3]))
    board.append(list(input_string[3:6]))
    board.append(list(input_string[6:9]))

    x_count = 0
    o_count = 0
    for row in board:
        x_count += row.count("X")
        o_count += row.count("O")

    is_valid = True
    # 다채워졌을 경우
    if x_count + o_count == 9:
        # O가 5개가 아니고 X가 4개가 아니면 무조건 invalid
        if x_count != 5 or o_count != 4:
            is_valid = False
        else:
            if not win_by_3_check(board, True, x_count, o_count):
                is_valid = False
    # 부족한 경우
    else:
        # O가 X보다 많으면 무조건 invalid
        if x_count < o_count:
            is_valid = False
        else:
            if not win_by_3_check(board, False, x_count, o_count):
                is_valid = False

    if is_valid:
        print("valid")
    else:
        print("invalid")
