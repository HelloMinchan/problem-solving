import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
memoization = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]


def w(a, b, c):
    # 기저 사례
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if memoization[a][b][c]:
        return memoization[a][b][c]

    if a < b < c:
        memoization[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return memoization[a][b][c]

    memoization[a][b][c] = (
        w(a - 1, b, c)
        + w(a - 1, b - 1, c)
        + w(a - 1, b, c - 1)
        - w(a - 1, b - 1, c - 1)
    )

    return memoization[a][b][c]


while 1:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break
    else:
        print(f"w({a}, {b}, {c}) = {w(a, b, c)}")