# 5:10 ~ 5:31 (21분)
import sys, heapq

input = sys.stdin.readline

N = int(input())
e_drinks = sorted(list(map(int, input().split())))

min_heap = []
max_heap = []

for e_drink in e_drinks[: N // 2]:
    heapq.heappush(min_heap, e_drink)

for e_drink in e_drinks[N // 2 :]:
    heapq.heappush(max_heap, -e_drink)


while min_heap and max_heap:
    e_drink1 = heapq.heappop(min_heap)
    e_drink2 = -heapq.heappop(max_heap)

    new_e_drink = (
        e_drink1 + e_drink2 / 2 if e_drink1 >= e_drink2 else e_drink2 + e_drink1 / 2
    )

    if not min_heap and not max_heap:
        print(new_e_drink)
    elif not min_heap and max_heap:
        heapq.heappush(min_heap, new_e_drink)
    elif min_heap and max_heap:
        heapq.heappush(max_heap, -new_e_drink)
    else:
        if len(min_heap) >= (max_heap):
            heapq.heappush(max_heap, -new_e_drink)
        else:
            heapq.heappush(min_heap, new_e_drink)