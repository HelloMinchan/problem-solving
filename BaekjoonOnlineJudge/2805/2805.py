import sys

input = sys.stdin.readline


def get_tree(cut_height):
    cut_tree = 0

    for tree in trees:
        if tree > cut_height:
            cut_tree += tree - cut_height
    
    return cut_tree


N, M = map(int, input().split())
trees = list(map(int, input().split()))

answer = 0
left = 0
right = max(trees)

while left <= right:
    mid = (left + right) // 2

    if M > get_tree(mid):        
        right = mid - 1
    else:
        answer = max(answer, mid)
        left = mid + 1

print(answer)
