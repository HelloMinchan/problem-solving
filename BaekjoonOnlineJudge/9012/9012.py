import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    paren = list(input().rstrip())

    stack = []
    isWrong = False
    for p in paren:
        if p == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                isWrong = True
                print("NO")
                break
    
    if not isWrong:
        print("NO" if stack else "YES")
        
