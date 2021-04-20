import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def DFS(con, vow):
    if len(stack) == L:
        if con >= 1 and vow >= 2:
            print("".join(stack))
        return

    for index in range(C):
        if not stack or stack[-1] < chars[index]:
            stack.append(chars[index])

            if chars[index] in ["a", "e", "i", "o", "u"]:
                DFS(con + 1, vow)
            else:
                DFS(con, vow + 1)

            stack.pop()


L, C = map(int, input().split())
chars = sorted(list(input().split()))
stack = []

DFS(0, 0)