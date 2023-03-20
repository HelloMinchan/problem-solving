def solution(files):
    answer = []

    total_sep_list = []
    for file_index, file in enumerate(files):
        start_num_index = len(file)
        end_num_index = 0

        sep_list = []
        num_flag = False
        for index, char in enumerate(file):
            if char.isdigit():
                num_flag = True
                start_num_index = min(start_num_index, index)
                end_num_index = max(end_num_index, index)
            if not char.isdigit() and num_flag:
                break

        sep_list.append(file[:start_num_index].upper())
        sep_list.append(file[start_num_index : end_num_index + 1])
        sep_list.append(file[end_num_index + 1 :])
        sep_list.append(file_index)

        total_sep_list.append(sep_list)

    total_sep_list.sort(key=lambda target: (target[0], int(target[1]), target[3]))

    for sep_list in total_sep_list:
        answer.append(files[sep_list[3]])

    return answer
