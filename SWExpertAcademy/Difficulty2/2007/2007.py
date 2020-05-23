t = int(input())
for case in range(t):
    str = input()
    length = 2
    first_last = 2
    second_last = 4
    while length <= 10:
        if str[0:first_last] == str[first_last:second_last]:
            break
        first_last += 1
        second_last += 2
        length += 1
    print('#{} {}'.format(case+1, length))
