t = int(input())
for case in range(t):
    num = list(map(int, input().split()))
    num.sort()
    num = round(sum(num[1:len(num)-1]) / 8)
    print('#{} {}'.format(case+1, num))
