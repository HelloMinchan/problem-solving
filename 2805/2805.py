import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
left = 0
right = max(trees)
maxCut = 0

while left <= right:
    getTree = 0
    mid = (left + right) // 2

    for tree in trees:
        if tree - mid < 0:
            continue
        getTree += tree - mid

    if getTree == M:
        print(mid)
        sys.exit()
    elif getTree < M:
        right = mid - 1
    else:
        if maxCut < mid:
            maxCut = mid
        left = mid + 1
        
print(maxCut)