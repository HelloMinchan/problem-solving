t = int(input())
for case in range(t):
    a, b = input().split()
    print('#{} {} {}'.format(case+1, int(a)//int(b), int(a)%int(b)))
