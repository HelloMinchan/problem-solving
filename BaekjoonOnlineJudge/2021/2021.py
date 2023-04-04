from collections import deque
import sys

input = sys.stdin.readline


def bfs(START, END):
    if START == END:
        return 0

    visit_station = [-1 for _ in range(N + 1)]
    visit_line = [False for _ in range(L + 1)]

    dq = deque()
    visit_station[START] = 0
    for line in lines[START]:
        visit_line[line] = True
        dq.append((START, line))

    while dq:
        station, line = dq.popleft()

        for next_station in stations[line]:
            if visit_station[next_station] != -1:
                continue

            if next_station == END:
                return visit_station[station]

            visit_station[next_station] = visit_station[station] + 1

            for next_line in lines[next_station]:
                if visit_line[next_line]:
                    continue

                dq.append((next_station, next_line))

    return -1


N, L = map(int, input().split())
lines = [list() for _ in range(N + 1)]
stations = [list() for _ in range(L + 1)]

for line in range(1, L + 1):
    for station in list(map(int, input().split()))[:-1]:
        lines[station].append(line)
        stations[line].append(station)

START, END = map(int, input().split())

print(bfs(START, END))
