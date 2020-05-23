num = int(input())
for i in range(num+1):
    n = int(i)
    if n == 0:
        print(1, end = ' ')
    else:
        print(2 ** n, end = ' ')
