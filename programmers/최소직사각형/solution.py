def solution(sizes):
    bigger_max = 0
    smaller_max = 0

    for size in sizes:
        bigger_max = max(bigger_max, max(size))
        smaller_max = max(smaller_max, min(size))

    return bigger_max * smaller_max