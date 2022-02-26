import sys

input = sys.stdin.readline


def find_rectangle(x, y):
    max_size = 100
    for i in range(100):
        if x + i > 100:
            break
        for j in range(100):
            if y + j > 100:
                break
            max_size = max(max_size, calculate_area(x, y, x + i, y + j))
    return max_size


def calculate_area(x, y, h, w):
    cnt = 0
    for i in range(x, h + 1):
        for j in range(y, w + 1):
            if not paper[i][j]:
                return 0
            else:
                cnt += 1
    return cnt


n = int(input())
paper = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

max_size = 100
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            max_size = max(max_size, find_rectangle(i, j))
print(max_size)