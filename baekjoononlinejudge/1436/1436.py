import sys
input = sys.stdin.readline

title = 666
N = int(input())

while(N):
    if '666' in str(title):
        N -= 1
    title += 1
print(title - 1)