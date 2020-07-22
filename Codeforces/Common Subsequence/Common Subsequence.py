import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for target in b:
        if target in a:
            print("YES")
            print(1, target)
            break
    else:
        print("NO")
