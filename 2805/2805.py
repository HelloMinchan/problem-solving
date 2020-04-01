import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
cut = max(trees) // 2
backCut1 = 0
backCut2 = 0
upAndDown = 0

while True:
    getTree = 0
    
    for tree in trees:
        if tree - cut < 0:
            continue
        getTree += tree - cut

    if M < getTree:
        if upAndDown == +1:
            print(backCut2)
            exit()
        upAndDown += 1
        cut = cut + (max(trees) - cut) // 2
    elif M > getTree:
        if upAndDown == -1:
            print(backCut2)
            exit()
        upAndDown -= 1
        cut = cut - (max(trees) - cut) // 2
    else:
        print(cut)
        exit()

    backCut2 = backCut1
    backCut1 = getTree

print(cut)