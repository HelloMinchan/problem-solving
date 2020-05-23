N = int(input())
for i in range(N):
    num = int(i) + 1
    if N % (num) == 0:
        print(num, end = ' ')
