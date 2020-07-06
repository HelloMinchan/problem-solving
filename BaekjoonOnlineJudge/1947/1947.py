import sys
input = sys.stdin.readline

N = int(input())

if N == 1:
    print(0)
    sys.exit(0)

before = 0
now = 1
answer = 1

for i in range(2, N):
    answer = (i * (now + before) % 1000000000)
    before = now
    now = answer 

print(answer % 1000000000)
