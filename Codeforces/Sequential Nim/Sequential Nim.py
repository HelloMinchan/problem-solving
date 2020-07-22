import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    s = list(map(int, input().split()))

    one = s.count(1)
    if one == n:
        if one % 2:
            print("First")
        else:
            print("Second")
    else:
        winner = True
        for num in s:
            if num == 1:
                winner = not winner
            else:
                break
        
        print("First" if winner else "Second")
