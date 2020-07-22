import sys
input = sys.stdin.readline

n = int(input())

if n % 8 == 1:
    print(1)
elif n % 8 == 2:
    print(2)
elif n % 8 == 3:
    print(3)
elif n % 8 == 4:
    print(4)
elif n % 8 == 5:
    print(5)
elif n % 8 == 6:
    print(4)
elif n % 8 == 7:
    print(3)
elif n % 8 == 0:
    print(2)
