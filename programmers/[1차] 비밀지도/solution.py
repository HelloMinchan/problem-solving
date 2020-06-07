def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        b1 = format(arr1[i], 'b')
        if len(b1) != n:
            while len(b1) != n:
                b1 = "0" + b1

        b2 = format(arr2[i], 'b')
        if len(b2) != n:
            while len(b2) != n:
                b2 = "0" + b2

        s = ""
        for j in range(n):
            if b1[j] == "1" or b2[j] == "1":
                s += "#"
            else:
                s += " "

        answer.append(s)

    return answer
