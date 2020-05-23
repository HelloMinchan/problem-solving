import sys
input = sys.stdin.readline


def quadTree(index):
    if index >= len(picture):
        return ""
    
    if picture[index] == "w":
        return "w"

    if picture[index] == "b":
        return "b"
    
    leftUp = quadTree(index + 1)
    index += len(leftUp)

    rightUp = quadTree(index + 1)
    index += len(rightUp)

    leftDown = quadTree(index + 1)
    index += len(leftDown)

    rightDown = quadTree(index + 1)
    index += len(rightDown)

    return "x" + leftDown + rightDown + leftUp + rightUp


C = int(input())

for _ in range(C):
    picture = input().rstrip()

    ans = quadTree(0)

    print(ans)