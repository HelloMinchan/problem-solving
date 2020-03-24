import sys
input = sys.stdin.readline


def backTracking(index, S, visit, printList):
    if len(printList) == 6:
        for i in range(len(printList) - 1):
            if printList[i] > printList[i + 1]:
                return
        print(*printList)
        return

    for i in range(index, len(S)):
        if not visit[i]:
            visit[i] = True
            printList.append(S[i])
            backTracking(i, S, visit, printList)

            printList.pop()
            visit[i] = False


while True:
    case = list(map(int, input().split()))
    k = case[0]
    if k == 0:
        exit()

    S = case[1:]

    printList = []
    
    visit = [False] * len(S)
    backTracking(0, S, visit, printList)
    print()