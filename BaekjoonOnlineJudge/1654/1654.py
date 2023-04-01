import sys

input = sys.stdin.readline


def cutting_lan_cables(cutting_length):
    lan_cable_count = 0

    for lan_cable in lan_cables:
        lan_cable_count += lan_cable // cutting_length

    return lan_cable_count


K, N = map(int, input().split())

lan_cables = [int(input()) for _ in range(K)]

answer = 0
left = 1
right = max(lan_cables)

while left <= right:
    mid = (left + right) // 2

    if cutting_lan_cables(mid) >= N:
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)
