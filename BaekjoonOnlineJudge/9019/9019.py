from collections import deque
import sys
input = sys.stdin.readline


def BFS(origin):
    dq = deque()
    dq.append(origin)

    while dq:
        target, order = dq.popleft()
        
        for i in range(4):
            tempTarget = target
            tempOrder = order

            if i == 0:
                tempTarget *= 2
                if tempTarget > 9999:
                    tempTarget %= 10000
                tempOrder = order + "D"

            if i == 1:
                tempTarget -= 1
                if tempTarget == -1:
                    tempTarget = 9999
                tempOrder = order + "S"
            
            n1000 = tempTarget // 1000
            n100 = tempTarget // 100 - n1000 * 10
            n10 = tempTarget // 10 - n1000 * 100 - n100 * 10
            n1 = tempTarget // 1 - n1000 * 1000 - n100 * 100 - n10 * 10

            if i == 2:
                tempTarget = (tempTarget // 1 - n1000 * 1000) * 10 + n1000

                tempOrder = order + "L"

            if i == 3:
                tempTarget //= 10
                tempTarget += n1 * 1000

                tempOrder = order + "R"
            
            if tempTarget == B:
                return tempOrder

            if not visit[tempTarget]:
                visit[tempTarget] = True
                dq.append((tempTarget, tempOrder))


T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    visit = [False] * 10001

    print(BFS((A, "")))
