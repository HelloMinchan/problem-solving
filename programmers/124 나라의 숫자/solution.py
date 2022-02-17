def solution(n):
    digits = ["1", "2", "4"]
    answer = ""

    while n > 0:
        n = n - 1
        answer = digits[n % 3] + answer
        n //= 3

    return answer