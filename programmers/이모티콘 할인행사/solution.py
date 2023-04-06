def dfs(start_emoticon_index, users, emoticons):
    global answer, stack, visit, discounts

    if len(stack) == len(emoticons):
        emoticon_plus_member = 0
        emoticon_sell_amount = 0

        for user in users:
            user_percent, user_amount = user
            buy_amount = 0

            for i in range(len(stack)):
                emoticon_price = emoticons[stack[i]]
                emoticon_discount = visit[i]

                if user_percent <= emoticon_discount:
                    emoticon_price -= emoticon_price * (emoticon_discount / 100)
                    buy_amount += emoticon_price

            if buy_amount >= user_amount:
                emoticon_plus_member += 1
            else:
                emoticon_sell_amount += buy_amount

        if answer[0] < emoticon_plus_member:
            answer[0] = emoticon_plus_member
            answer[1] = emoticon_sell_amount
        elif answer[0] == emoticon_plus_member and answer[1] < emoticon_sell_amount:
            answer[0] = emoticon_plus_member
            answer[1] = emoticon_sell_amount

        return

    for discount_index in range(4):
        for emoticon_index in range(start_emoticon_index, len(emoticons)):
            if visit[emoticon_index] == 0:
                visit[emoticon_index] = discounts[discount_index]
                stack.append(emoticon_index)
                dfs(emoticon_index + 1, users, emoticons)
                visit[emoticon_index] = 0
                stack.pop()


def solution(users, emoticons):
    global answer, stack, visit, discounts
    answer = [0, 0]

    visit = [0 for _ in range(len(emoticons))]
    discounts = [10, 20, 30, 40]
    stack = []

    dfs(0, users, emoticons)

    return answer
