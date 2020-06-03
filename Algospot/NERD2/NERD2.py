import sys, bisect
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    ans = 0
    nerds = []
    numOfNerd = 0
    N = int(input())
    
    for _ in range(N):  
        p, q = map(int, input().split())

        i = bisect.bisect(nerds, (p, q))

        if i == numOfNerd or q > nerds[i][1]:
            nerds.insert(i , (p, q))
            numOfNerd += 1
            
            i -= 1
            while i >= 0:
                if q <= nerds[i][1]:
                    break
                
                nerds.pop(i)
                numOfNerd -= 1
                i -= 1
                
        ans += numOfNerd

    print(ans)