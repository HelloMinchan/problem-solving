import sys
input = sys.stdin.readline


def pCheck(forth, back, p):
    if p == '<':
        return forth < back
    return forth > back


def DFS(length, num):
    global isFirst, maxNum, minNum

    if length == k + 1:
        if isFirst:
            minNum = num
            isFirst = False
        else:
            maxNum = num
        return

    for i in range(10):
        if not visit[i]:
            if not length or pCheck(int(num[-1]), i, inequality[length - 1]):
                visit[i] = True
                DFS(length + 1, num + str(i))
                visit[i] = False


k = int(input())

inequality = input().rstrip().split()
visit = [False] * 10
isFirst = True
maxNum = ""
minNum = ""

DFS(0, "")

print(maxNum)
print(minNum)
