def solution(s):
    answer, start = '', 0

    for i in range(len(s)):
        if s[i] == ' ':
            answer += s[i]
            start = i+1
        elif i == start:
            answer += s[i].upper()
        else:
            answer += s[i].lower()

    return answer
