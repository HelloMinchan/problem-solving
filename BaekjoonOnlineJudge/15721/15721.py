# 3:01 ~ 3:24 (23분)
import sys

input = sys.stdin.readline

A = int(input())
T = int(input())
signal = int(input())
t_count = 0
person = -1

pre_song = [1, 0, 1, 0]
post_song = [0, 1]

pre_song_count = 3
post_song_count = 1
post_song_cycle_1 = 0
post_song_cycle_2 = 0
cycle = 2

while 1:
    person = (person + 1) % A

    if pre_song_count >= 0:
        if pre_song[pre_song_count] == signal:
            t_count += 1
        pre_song_count -= 1
    else:
        if post_song_cycle_1 != cycle:
            if post_song[0] == signal:
                t_count += 1
            post_song_cycle_1 += 1
        elif post_song_cycle_2 != cycle:
            if post_song[1] == signal:
                t_count += 1
            post_song_cycle_2 += 1

            if post_song_cycle_2 == cycle:
                pre_song_count = 3
                post_song_cycle_1 = 0
                post_song_cycle_2 = 0
                cycle += 1

    if t_count == T:
        print(person)
        break
