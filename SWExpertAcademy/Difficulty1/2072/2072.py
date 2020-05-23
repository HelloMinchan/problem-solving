t = int(input())
for case in range(t):
    result = 0
    temp = input()
    arr = temp.split()
    arr = [int(x) for x in arr]
    i =0
    while i < 10:
        if (arr[i] % 2) == 1: 
            result += arr[i]
        i +=1
    print("#{} {}".format(case+1, result))
