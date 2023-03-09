def convert_minute(time):
    hour, minute = time.split(":")

    return int(hour) * 60 + int(minute)


def convert_sharp(melody):
    melody = melody.replace("C#", "c")
    melody = melody.replace("D#", "d")
    melody = melody.replace("F#", "f")
    melody = melody.replace("G#", "g")
    melody = melody.replace("A#", "a")

    return melody


def solution(m, musicinfos):
    answer_time = 0
    answer_name = ""
    m = convert_sharp(m)

    for info in musicinfos:
        start_time, end_time, song_name, melody = info.split(",")

        play_time = abs(convert_minute(end_time) - convert_minute(start_time))
        melody = convert_sharp(melody)
        melody = melody * (play_time // len(melody)) + melody[: play_time % len(melody)]

        if m in melody:
            if answer_time < len(melody):
                answer_time = len(melody)
                answer_name = song_name

    return answer_name if answer_name else "(None)"
