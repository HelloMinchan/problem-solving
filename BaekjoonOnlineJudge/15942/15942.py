from collections import deque
import sys
input = sys.stdin.readline


def getUp():
    global up, upCount

    t = p
    while 1:
        t >>= 1
        if t == 0:
            break
        up.append(t)
    
    up = list(reversed(up))

    if len(up) >= k:
        print(-1)
        sys.exit(0)
    
    for i in up:
        upCount += 1
        ans[i] = upCount


def DFS(v):
    global downCount
    
    downCount -= 1
    ans[v] = downCount

    if v * 2 <= N:
        DFS(v * 2)
    if v * 2 + 1 <= N:
        DFS(v * 2 + 1)


def getDown():
    global downCount

    downCount = N
    
    if 2 * p <= N:
        DFS(2 * p)
    if 2 * p + 1 <= N:
        DFS(2 * p + 1)
    if downCount < k:
        print(-1)
        sys.exit(0)


def upHeap(x):
    while x > 1:
        if heap[x // 2] <= heap[x]:
            break
        heap[x], heap[x // 2] = heap[x // 2], heap[x]
        x >>= 1


def insert(v):
    global heapN
    heapN += 1
    heap[heapN] = v
    upHeap(heapN)


N = int(input())
k, p = map(int, input().split())

ans = [0] * 202020
upCount = 0
downCount = 0
up = []

heapN = 0
heap = [0] * 202020

ans[p] = k
getUp()
getDown()

dq = deque()

for i in range(upCount + 1, downCount + 1):
    if i == k:
        continue
    dq.append(i)

for i in range(1, N + 1):
    if ans[i]:
        continue
    ans[i] = dq.popleft()

    for i in range(1, N + 1):
        print(ans[i])
