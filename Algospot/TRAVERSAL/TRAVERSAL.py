import sys
input = sys.stdin.readline


def printPostorder(preorder, inorder):
    if not len(preorder):
        return

    root = preorder[0]
    mid = inorder.index(root)

    printPostorder(preorder[1:mid + 1], inorder[0:mid])
    printPostorder(preorder[mid + 1:len(preorder)], inorder[mid + 1:len(preorder)])

    print(root, end=" ")


C = int(input())
for _ in range(C):
    N = int(input())

    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    printPostorder(preorder, inorder)
    print()