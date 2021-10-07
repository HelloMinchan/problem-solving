import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    r,b,d=map(int,input().split())

    if d == 0:
        if r == b:
            print("YES")
        else:
            print("NO")
    else:
        if r<b:
            if b / r <= d+1:
                print("YES")
            else:
                print("NO")
        else:
            if r / b <= d+1:
                print("YES")
            else:
                print("NO")