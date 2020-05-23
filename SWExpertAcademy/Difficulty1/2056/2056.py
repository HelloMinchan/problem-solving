t = int(input())
for case in range(t):
    valid = 0
    temp = input()
    str_year = temp[0:4]
    str_month = temp[4:6]
    str_day = temp[6:8]
    month = int(temp[4:6])
    day = int(temp[6:8])

    if month >= 1 and month <= 12:
        if month == 2:
            if day < 1 or day > 28:
                valid = -1
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day < 1 or day > 30:
                valid = -1
        else:
            if day < 1 or day > 31:
                valid = -1
    else:
        valid = -1

    if valid == 0:
        print('#{} {}/{}/{}'.format(case+1, str_year, str_month, str_day))
    else:
        print('#{} {}'.format(case+1, valid))
