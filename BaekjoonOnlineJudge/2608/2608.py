import sys

input = sys.stdin.readline

roma_to_arabia_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def convert_to_arabia(roma_number):
    roma_number_list = list(roma_number)
    arabia_number = 0
    index = 0

    while index <= len(roma_number_list) - 1:
        if index < len(roma_number_list) - 1 and roma_number_list[index] == "C":
            if roma_number_list[index + 1] in [
                "M",
                "D",
            ]:
                arabia_number += (
                    roma_to_arabia_dict[roma_number_list[index + 1]]
                    - roma_to_arabia_dict[roma_number_list[index]]
                )
                index += 2
                continue
        elif index < len(roma_number_list) - 1 and roma_number_list[index] == "X":
            if roma_number_list[index + 1] in ["C", "L"]:
                arabia_number += (
                    roma_to_arabia_dict[roma_number_list[index + 1]]
                    - roma_to_arabia_dict[roma_number_list[index]]
                )
                index += 2
                continue
        elif index < len(roma_number_list) - 1 and roma_number_list[index] == "I":
            if roma_number_list[index + 1] in ["X", "V"]:
                arabia_number += (
                    roma_to_arabia_dict[roma_number_list[index + 1]]
                    - roma_to_arabia_dict[roma_number_list[index]]
                )
                index += 2
                continue

        arabia_number += roma_to_arabia_dict[roma_number_list[index]]
        index += 1

    return arabia_number


def convert_to_roma(arabia_number):
    arabia_number_list = list(reversed(str(arabia_number)))
    roma_number = ""
    index = 0

    for index in range(len(arabia_number_list) - 1, -1, -1):
        target_number = int(arabia_number_list[index])

        if index == 3:
            for _ in range(target_number):
                roma_number += "M"
        elif index == 2:
            if target_number == 9:
                roma_number += "CM"
            elif target_number >= 5:
                roma_number += "D"
                for _ in range(target_number - 5):
                    roma_number += "C"
            elif target_number == 4:
                roma_number += "CD"
            else:
                for _ in range(target_number):
                    roma_number += "C"
        elif index == 1:
            if target_number == 9:
                roma_number += "XC"
            elif target_number >= 5:
                roma_number += "L"
                for _ in range(target_number - 5):
                    roma_number += "X"
            elif target_number == 4:
                roma_number += "XL"
            else:
                for _ in range(target_number):
                    roma_number += "X"
        else:
            if target_number == 9:
                roma_number += "IX"
            elif target_number >= 5:
                roma_number += "V"
                for _ in range(target_number - 5):
                    roma_number += "I"
            elif target_number == 4:
                roma_number += "IV"
            else:
                for _ in range(target_number):
                    roma_number += "I"

    return roma_number


roma_number1 = input().rstrip()
roma_number2 = input().rstrip()

total_arabia_number = convert_to_arabia(roma_number1) + convert_to_arabia(roma_number2)

print(total_arabia_number)

print(convert_to_roma(total_arabia_number))
