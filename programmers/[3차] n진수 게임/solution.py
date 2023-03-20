def convert_number(number, n):
    if number == 0:
        return "0"

    NUMBERS = "0123456789ABCDEF"
    converted_number = ""

    while number > 0:
        number, mod = divmod(number, n)
        converted_number += NUMBERS[mod]

    return converted_number[::-1]


def solution(n, t, m, p):
    converted_number = ""
    for number in range(t * m):
        converted_number += convert_number(number, n)

    return converted_number[p - 1 : t * m : m]
