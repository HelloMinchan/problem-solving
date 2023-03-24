def solution(lottos, win_nums):
    MAXIMUM_LOTTO_NUMBER = 6

    equals_lotto_number = 0

    for number in lottos:
        if number in win_nums:
            equals_lotto_number += 1

    lost_number = lottos.count(0)

    maximum_rank = MAXIMUM_LOTTO_NUMBER - equals_lotto_number - lost_number + 1
    minimum_rank = MAXIMUM_LOTTO_NUMBER - equals_lotto_number + 1

    return [
        maximum_rank if maximum_rank <= 6 else 6,
        minimum_rank if minimum_rank <= 6 else 6,
    ]
