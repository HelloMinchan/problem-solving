import sys

input = sys.stdin.readline

day_to_eng_dict = {
    1 : "MON",
    2 : "TUE",
    3 : "WED",
    4 : "THU",
    5 : "FRI",
    6 : "SAT",
    0 : "SUN"
}

day_of_month_dict = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
}

x, y = map(int,input().split())

sum_day = y

if x > 1:
    for month in range(1, x):
        sum_day += day_of_month_dict[month]


print(day_to_eng_dict[(sum_day % 7)])