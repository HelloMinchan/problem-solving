def solution(money):
    memoization1 = [0 for _ in range(len(money))]
    memoization2 = [0 for _ in range(len(money))]

    for i, cost in enumerate(money[: len(money) - 1]):
        if i == 0:
            memoization1[0] = cost
        elif i == 1:
            memoization1[1] = 0
        else:
            if i - 3 >= 0:
                if cost + memoization1[i - 2] > cost + memoization1[i - 3]:
                    memoization1[i] = cost + memoization1[i - 2]
                else:
                    memoization1[i] = cost + memoization1[i - 3]
            else:
                memoization1[i] = cost + memoization1[i - 2]

    for i, cost in enumerate(money):
        if i == 0:
            memoization2[0] = 0
        elif i == 1:
            memoization2[1] = cost
        else:
            if i - 3 >= 0:
                if cost + memoization2[i - 2] > cost + memoization2[i - 3]:
                    memoization2[i] = cost + memoization2[i - 2]
                else:
                    memoization2[i] = cost + memoization2[i - 3]
            else:
                memoization2[i] = cost + memoization2[i - 2]

    return max(max(memoization1), max(memoization2))