import heapq


def convert_minute_time(time):
    hour, minute = time.split(":")

    return int(hour) * 60 + int(minute)


def convert_origin_time(time):
    hour = time // 60
    minute = time % 60

    if hour < 10:
        hour = "0" + str(hour)
    if minute < 10:
        minute = "0" + str(minute)

    return str(hour) + ":" + str(minute)


def solution(n, t, m, timetable):
    answer_time = 0

    hq = []
    for krew_time in timetable:
        heapq.heappush(hq, convert_minute_time(krew_time))

    bus_stop_time = convert_minute_time("09:00")

    for bus_stop_count in range(1, n + 1):
        board_krew = []

        for _ in range(m):
            if hq and hq[0] <= bus_stop_time:
                board_krew.append(heapq.heappop(hq))

        if bus_stop_count == n:
            if board_krew:
                if len(board_krew) == m:
                    answer_time = board_krew[-1] - 1
                else:
                    answer_time = bus_stop_time
            else:
                answer_time = bus_stop_time

        bus_stop_time += t

    return convert_origin_time(answer_time)
