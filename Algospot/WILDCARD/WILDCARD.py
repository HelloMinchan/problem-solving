import sys
input = sys.stdin.readline


def inspect(i, j):
    if i == len(wildStr) and j == len(compareStr):
        return True
    
    if i == len(wildStr) and j != len(compareStr):
        return False
    
    if i != len(wildStr) and j == len(compareStr):
        starCheck = True

        for k in range(i, len(wildStr)):
            if wildStr[k] != "*":
                starCheck = False
                break

        if starCheck:
            return True
        else:
            return False
    
    if wildStr[i] == compareStr[j]:
        return inspect(i + 1, j + 1)
    
    if wildStr[i] == "?":
        return inspect(i + 1, j + 1)
    
    if wildStr[i] == "*":
        if i == len(wildStr) - 1:
            return True

        if wildStr[i + 1] == "*":
            for k in range(i + 1, len(wildStr)):
                if wildStr[k] == "*":
                    continue
                else:
                    if k == len(wildStr) - 1:
                        if wildStr[k] == compareStr[-1]:
                            return True
                        else:
                            return False
                    else:
                        return inspect(k, j)

            return inspect(i + 1, j)

        if wildStr[i + 1] == compareStr[j]:
            return inspect(i + 1, j)
        else:
            return inspect(i, j + 1)


C = int(input())
wildStr = ""
compareStr = ""

for _ in range(C):
    wildStr = input().rstrip()
    N = int(input())

    memoization = []

    for _ in range(N):
        compareStr = input().rstrip()

        if inspect(0, 0):
            memoization.append(compareStr)
    
    for i in range(len(memoization)):
        print(memoization[i])