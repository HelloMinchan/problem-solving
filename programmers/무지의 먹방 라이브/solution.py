def solution(food_times, k):
    food_length = len(food_times)
    foods = []
    for index, food in enumerate(food_times):
        foods.append((food, index + 1))

    foods.sort()

    now_food = before_food = 0
    for index, food_info in enumerate(foods):
        food = food_info[0]

        if food > before_food:
            now_food = food

            if k >= (now_food - before_food) * food_length:
                k -= (now_food - before_food) * food_length
                before_food = now_food
            else:
                return sorted(foods[index:], key=lambda food_info: food_info[1])[
                    k % food_length
                ][1]

        food_length -= 1

    return -1
