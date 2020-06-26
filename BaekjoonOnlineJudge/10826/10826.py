import sys
input = sys.stdin.readline

N = int(input())

N //= 1000000000
back2 = 0
back1 = 1
now = 0
for i in range(2, N + 1):
    now = (back2 + back1) % 1000000

    back1 = back2
    back2 = now

print(back1 + back2 % 1000000)
