t = int(input())
for case in range(t):
    temp = input()
    if temp == temp[::-1]:
        print('#{} {}'.format(case+1, 1))
    else:
    	print('#{} {}'.format(case+1, 0))
