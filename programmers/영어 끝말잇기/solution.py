def solution(n, words):
    hash_word = dict()

    person = 0
    count = 1
    for i, word in enumerate(words):
        person += 1
        if person == n + 1:
            person = 1
            count += 1

        if i:
            if words[i-1][-1] != words[i][0]:
                return [person, count]
        if hash_word.get(word, 0):
            return [person, count]
        else:
            hash_word[word] = 1

    return [0, 0]
