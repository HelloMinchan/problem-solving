for case in range((int(input()))):
    _ = int(input())
    n = list(map(int, input().split()))
    print(f'#{case+1}', end=' ')
    n.sort()
    print(*n)
