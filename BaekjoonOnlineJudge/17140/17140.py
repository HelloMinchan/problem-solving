from collections import defaultdict
import sys

input = sys.stdin.readline

r, c, k = map(int, input().split())
r -= 1
c -= 1

arr = [list(map(int, input().split())) for _ in range(3)]

for time in range(0, 101):
    if r < len(arr) and c < len(arr[0]) and arr[r][c] == k:
        print(time)
        break
    else:
        is_C = False
        if len(arr) < len(arr[0]):
            is_C = True
            arr = [list(col) for col in zip(*arr)][:]

        max_length = 0
        for index, row in enumerate(arr):
            number_dict = defaultdict(int)
            for number in row:
                if number != 0:
                    number_dict[number] += 1
            temp_arr = sorted(
                number_dict.items(), key=lambda number: (number[1], number[0])
            )

            temp_arr_length = min(50, len(temp_arr))

            arr[index] = []
            for i in range(temp_arr_length):
                arr[index] += list(temp_arr[i])

            max_length = max(max_length, len(arr[index]))

        for index, row in enumerate(arr):
            if len(row) < max_length:
                for _ in range(max_length - len(row)):
                    arr[index].append(0)

        if is_C:
            arr = [list(col) for col in zip(*arr)][:]
else:
    print(-1)
