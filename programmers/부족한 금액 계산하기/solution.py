def solution(price, money, count):
    total_money = 0
    for multi in range(1, count + 1):
        total_money += price * multi

    return abs(money - total_money) if money - total_money < 0 else 0