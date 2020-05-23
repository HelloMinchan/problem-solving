t = int(input())
for case in range(t):
    temp = input();
    arr = temp.split();
    arr = [int(x) for x in arr]
    i = 0
    ave = 0
    while i < 10:
        ave += arr[i]
        i += 1
    print('#{} {}'.format(case+1, round(ave/10)))
