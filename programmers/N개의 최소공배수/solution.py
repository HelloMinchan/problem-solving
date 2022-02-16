# 2:30 ~
def gcd(a, b):
    return b if not a % b else gcd(b, a % b)


def solution(arr):
    answer = arr[0]

    for num in arr[1:]:
        answer = answer * num // gcd(answer, num)

    return answer