def solution(enroll, referral, seller, amount):
    name_tree = dict()
    result_dict = dict()
    for i in range(len(enroll)):
        name_tree[enroll[i]] = referral[i]
        result_dict[enroll[i]] = 0

    for i in range(len(seller)):
        seller_name = seller[i]
        sell_money = amount[i] * 100
        upper_money = int(sell_money * 0.1)

        result_dict[seller_name] += sell_money - upper_money

        while name_tree[seller_name] != "-":
            seller_name = name_tree[seller_name]

            if upper_money == 0:
                break

            sell_money = upper_money
            upper_money = int(sell_money * 0.1)

            result_dict[seller_name] += sell_money - upper_money

    return list(result_dict.values())
