def solution(new_id):
    # process 1
    new_id = new_id.lower()

    # process 2
    processed_id = ""
    for char in new_id:
        if (
            char.isalpha()
            or char.isdigit()
            or char == "-"
            or char == "_"
            or char == "."
        ):
            processed_id += char

    # process 3
    if processed_id:
        new_processed_id = ""
        is_before_dot = False

        for char in processed_id:
            if char == ".":
                if is_before_dot:
                    continue
                else:
                    new_processed_id += char
                    is_before_dot = True
            else:
                new_processed_id += char
                is_before_dot = False

        processed_id = new_processed_id

    # process 4
    if processed_id:
        if processed_id[0] == ".":
            processed_id = processed_id[1:]

        if processed_id:
            if processed_id[-1] == ".":
                processed_id = processed_id[: len(processed_id) - 1]

    # process 5
    if processed_id == "":
        processed_id += "a"

    # process 6
    if len(processed_id) >= 16:
        processed_id = processed_id[:15]

        if processed_id[-1] == ".":
            processed_id = processed_id[: len(processed_id) - 1]

    # process 7
    if len(processed_id) <= 2:
        last_char = processed_id[-1]

        while len(processed_id) < 3:
            processed_id += last_char

    return processed_id
