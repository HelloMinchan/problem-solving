import sys

input = sys.stdin.readline

x, y = map(int, input().split())

days_in_month = [
    0,
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
]

day_to_string = [
    "SUN",
    "MON",
    "TUE",
    "WED",
    "THU",
    "FRI",
    "SAT"
]

total_days = y

for month in range(1, x):
    total_days += days_in_month[month]

print(day_to_string[total_days % 7])