def solution(records):
    ENTER_OPER = "Enter"
    LEAVE_OPER = "Leave"
    CHANGE_OPER = "Change"

    answer = []
    name_dict = dict()

    for record in records:
        record_info = record.split(" ")

        if record_info[0] == ENTER_OPER:
            name_dict[record_info[1]] = record_info[2]
        elif record_info[0] == CHANGE_OPER:
            name_dict[record_info[1]] = record_info[2]

    for record in records:
        record_info = record.split(" ")

        if record_info[0] == ENTER_OPER:
            answer.append(f"{name_dict[record_info[1]]}님이 들어왔습니다.")
        elif record_info[0] == LEAVE_OPER:
            answer.append(f"{name_dict[record_info[1]]}님이 나갔습니다.")

    return answer
