def get_distance(x1, y1, x2, y2):
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5


def solution(numbers, hand):
    answer = ""
    keypad_location = dict()
    keypad_location["1"] = (0, 0)
    keypad_location["2"] = (0, 1)
    keypad_location["3"] = (0, 2)
    keypad_location["4"] = (1, 0)
    keypad_location["5"] = (1, 1)
    keypad_location["6"] = (1, 2)
    keypad_location["7"] = (2, 0)
    keypad_location["8"] = (2, 1)
    keypad_location["9"] = (2, 2)
    keypad_location["*"] = (3, 0)
    keypad_location["0"] = (3, 1)
    keypad_location["#"] = (3, 2)

    left_location = keypad_location["*"]
    right_location = keypad_location["#"]

    for number in numbers:
        number = str(number)

        if number in ["1", "4", "7"]:
            answer += "L"
            left_location = keypad_location[number]
        elif number in ["3", "6", "9"]:
            answer += "R"
            right_location = keypad_location[number]
        else:
            location = keypad_location[number]

            left_distance = get_distance(*left_location, *location)
            right_distance = get_distance(*right_location, *location)

            if left_distance < right_distance:
                answer += "L"
                left_location = location
            elif left_distance > right_distance:
                answer += "R"
                right_location = location
            else:
                if hand == "left":
                    answer += "L"
                    left_location = location
                else:
                    answer += "R"
                    right_location = location

    return answer
