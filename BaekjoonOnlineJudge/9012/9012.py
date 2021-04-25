import sys

input = sys.stdin.readline

def isCorrect(parens):
    stack = []

    for paren in parens:
        if not stack:
            stack.append(paren)
        else:
            if paren == ")":
                if not stack or stack[-1] != "(":
                    return "NO"
                else:
                    stack.pop()
            else:
                stack.append(paren)
    
    if stack:
        return "NO"
    else:
        return "YES"



T = int(input())

for _ in range(T):
    parens = list(input().rstrip())
    
    print(isCorrect(parens))