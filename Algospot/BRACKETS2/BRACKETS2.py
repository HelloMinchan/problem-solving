import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    brackets = list(input().rstrip())
    stack = []
    isMatched = True

    for bracket in brackets:
        if not len(stack):
            stack.append(bracket)
            continue
        if bracket == "(" or bracket == "{" or bracket == "[":
            stack.append(bracket)
            continue
        if bracket == ")" or bracket == "}" or bracket == "]":
            if bracket == ")":
                if stack.pop() != "(":
                    isMatched = False
                    break
            elif bracket == "}":
                if stack.pop() != "{":
                    isMatched = False
                    break
            else:
                if stack.pop() != "[":
                    isMatched = False
                    break
    
    if len(stack):
        isMatched = False
    
    print("YES" if isMatched else "NO")