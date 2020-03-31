import sys
from idlelib.idle_test.test_searchengine import GetTest
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
cut = max(trees) // 2
recordCut = []

while True:
    getTree = 0
    
    for tree in trees:
        if tree - cut < 0:
            continue
        getTree += tree - cut

    if M == getTree:
        print(cut)
        exit()

    if M < getTree:
        cut = cut + (max(trees) - cut) // 2
        recordCut.append(cut)
    
    if M > getTree:
        cut //= 2
        recordCut.append(cut)

print(cut)