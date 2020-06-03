import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    ans = 0
    N = int(input())
    people = [list(map(int,input().split())) for _ in range(N)]
    nerds = []
    numOfNerd = 0

    for p, q in people:
        if not len(nerds):
            nerds.append((p,q))
            ans = numOfNerd = 1
            continue

        for i, nerd in enumerate(nerds):
            if p > nerd[0] or q > nerd[1]:
                if p > nerd[0] and q > nerd[1]:
                    nerds.pop(i)
                    nerds.insert(i,(p,q))
                    break
        else:
            nerds.append((p,q))
            numOfNerd += 1
            
        ans += numOfNerd

    print(ans)