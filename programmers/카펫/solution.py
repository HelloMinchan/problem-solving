# 2:01 ~ 2:23 (22분)
def solution(brown, yellow):
    answer = []

    # i는 세로, j는 가로
    for i in range(1, 5001):
        for j in range(i, 5001):
            if brown == (i - 2) * 2 + (j - 2) * 2 + 4 and yellow == (i - 2) * (j - 2):
                answer.append(j)
                answer.append(i)
                break

    return answer