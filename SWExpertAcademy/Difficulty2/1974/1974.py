for case in range((int(input()))):
    sdk = list(list(map(int, input().split())) for _ in range(9))
    t_sdk = list(zip(*sdk))
    t_sdk = list(list(t_sdk[x]) for x in range(9))
    answer = 1
    move = 0
    tot = 0
    col = 0
    for repeat in range(3):
        for row in range(9):
            move += 1
            tot += sum(sdk[row][col:col+3])
            if move%3 == 0:
                if tot != 45:
                    answer = 0
                    break
                else:
                    move = 0
                    tot = 0
        col += 3
    if answer == 1:
        for row in range(9):
            for col in range(9):
                sdk[row].sort()
                t_sdk[row].sort()
                if sdk[row][col] != col+1 or t_sdk[row][col] != col+1:
                    answer = 0
                    break
    print(f'#{case+1} {answer}')
