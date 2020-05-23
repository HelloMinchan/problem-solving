t = int(input())
for case in range(t):
    temp = input()
    arr = temp.split()
    arr = [int(x) for x in arr]
    if arr[0] == arr[1]:
        sign = '='
    elif arr[0] > arr[1]:
        sign = '>'
    else:
        sign = '<'
    print('#{} {}'.format(case+1, sign))
