import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def is_bad_seq(answer):
    for i in range(1, len(answer) // 2 + 1):
        if answer[-i:] == answer[-2 * i : -i]:
            return True

    return False


def dfs():
    if is_bad_seq(answer):
        return

    if len(answer) == N:
        print(*answer, sep="")
        sys.exit(0)

    for i in range(3):
        answer.append(nums[i])
        dfs()
        answer.pop()


N = int(input())

nums = [1, 2, 3]
answer = []

dfs()
