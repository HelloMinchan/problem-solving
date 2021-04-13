import sys

input = sys.stdin.readline


def lower_bound(stock_price):
    left = 0
    right = len(memoization) - 1

    while left < right:
        mid = (left + right) // 2

        if memoization[mid] < stock_price:
            left = mid + 1
        else:
            right = mid

    return right


def isPossible():
    for stock_price in stock_prices:
        if memoization[-1] < stock_price:
            memoization.append(stock_price)
        else:
            index = lower_bound(stock_price)

            memoization[index] = stock_price

    if len(memoization) - 1 >= K:
        return 1
    else:
        # 의심을 더 줄이기 위해서, 주식을 살 때마다 맨 처음을 제외하고는 바로 직전에 주식을 샀을 때보다 가격이 올라갔을 때만 사기로 했다.
        if len(memoization) - 1 == K - 1 and memoization[1] != stock_prices[0]:
            return 1
        return 0


T = int(input())

for case_number in range(1, T + 1):
    N, K = map(int, input().split())
    stock_prices = list(map(int, input().split()))
    memoization = [0]

    print(f"Case #{case_number}")
    print(isPossible())
