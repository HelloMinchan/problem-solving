import sys


def solution(s):
    if len(s) == 1:
        return 1

    answer = sys.maxsize

    for length in range(1, len(s)):
        temp_string = ""
        before_string = ""
        overlap_count = 1

        for index in range(0, len(s), length):
            now_string = s[index : index + length]

            if before_string != "":
                if before_string == now_string:
                    overlap_count += 1
                else:
                    if overlap_count == 1:
                        temp_string += before_string
                    else:
                        temp_string += str(overlap_count) + before_string

                    overlap_count = 1

            before_string = now_string

        if overlap_count == 1:
            temp_string += before_string
        else:
            temp_string += str(overlap_count) + before_string

        answer = min(answer, len(temp_string))

    return answer
