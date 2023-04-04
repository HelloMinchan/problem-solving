from collections import defaultdict
import bisect


def get_word_count(word_list, left_word, right_word):
    return bisect.bisect_right(word_list, right_word) - bisect.bisect_left(
        word_list, left_word
    )


def solution(words, queries):
    answer = []

    word_length_dict = defaultdict(list)
    reverse_word_length_dict = defaultdict(list)

    for word in words:
        length = len(word)
        word_length_dict[length].append(word)
        reverse_word_length_dict[length].append(word[::-1])

    for key in word_length_dict.keys():
        word_length_dict[key].sort()
        reverse_word_length_dict[key].sort()

    for query in queries:
        length = len(query)
        if query[0] == "?":
            answer.append(
                get_word_count(
                    reverse_word_length_dict[length],
                    query[::-1].replace("?", "a"),
                    query[::-1].replace("?", "z"),
                )
            )
        else:
            answer.append(
                get_word_count(
                    word_length_dict[length],
                    query.replace("?", "a"),
                    query.replace("?", "z"),
                )
            )

    return answer
