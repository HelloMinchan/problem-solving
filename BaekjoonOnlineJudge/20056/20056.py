from collections import deque
import sys

input = sys.stdin.readline


dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

is_all_same_direct_way = [0, 2, 4, 6]
is_not_all_same_direct_way = [1, 3, 5, 7]


def create_divided_fireball(r, c, m, s, ways):
    for way in ways:
        fireball_info_queue.append((r, c, m, s, way))


def divide_fireball(r, c, fireball_infos):
    total_m = 0
    total_s = 0

    is_all_same_direct = 0

    for fireball_info in fireball_infos:
        m, s, d = fireball_info
        total_m += m
        total_s += s

        if d % 2 == 0:
            is_all_same_direct += 1
        else:
            is_all_same_direct -= 1

    total_m //= 5

    if total_m == 0:
        return

    total_s //= len(fireball_infos)

    if abs(is_all_same_direct) == len(fireball_infos):
        create_divided_fireball(r, c, total_m, total_s, is_all_same_direct_way)
    else:
        create_divided_fireball(r, c, total_m, total_s, is_not_all_same_direct_way)


def move_fireball():
    field = [[[] for _ in range(N)] for _ in range(N)]

    while fireball_info_queue:
        r, c, m, s, d = fireball_info_queue.popleft()

        next_r = (r + dy[d] * s) % N
        next_c = (c + dx[d] * s) % N

        field[next_r][next_c].append((m, s, d))

    for r in range(N):
        for c in range(N):
            if len(field[r][c]) >= 2:
                divide_fireball(r, c, field[r][c])
            elif len(field[r][c]) == 1:
                m, s, d = field[r][c][0]
                fireball_info_queue.append((r, c, m, s, d))


N, M, K = map(int, input().split())

fireball_info_queue = deque()
for _ in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    fireball_info_queue.append((r - 1, c - 1, m, s, d))

for _ in range(K):
    move_fireball()


answer = 0
while fireball_info_queue:
    r, c, m, s, d = fireball_info_queue.popleft()

    answer += m

print(answer)
