from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())

location_dict = defaultdict(int)
answer = 0

for _ in range(N):
    cow_number, location = map(int, input().split())
    location += 1

    if location_dict[cow_number] == 0:
        location_dict[cow_number] = location
    elif location_dict[cow_number] == 1:
        if location == 2:
            answer += 1
        location_dict[cow_number] = location
    else:
        if location == 1:
            answer += 1
        location_dict[cow_number] = location

print(answer)
