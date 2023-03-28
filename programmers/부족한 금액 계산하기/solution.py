def solution(price, money, max_count):
    for count in range(1, max_count + 1):
        money -= price * count

    if money < 0:
        return -money
    else:
        return 0
