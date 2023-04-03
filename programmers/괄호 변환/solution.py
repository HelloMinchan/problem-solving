import sys

sys.setrecursionlimit(10**7)


def dfs(p):
    temp_string = ""

    if p == "":
        return ""

    stack = []
    is_u_right = True
    left = 0
    right = 0

    u_index = 0
    while u_index < len(p):
        if p[u_index] == "(":
            left += 1
            stack.append(p[u_index])

            if left == right:
                u_index += 1
                break
        else:
            right += 1

            if stack and stack[-1] == "(":
                stack.pop()
            else:
                is_u_right = False

            if left == right:
                u_index += 1
                break

        u_index += 1

    if is_u_right:
        temp_string += p[:u_index]

        if u_index < len(p):
            temp_string += dfs(p[u_index:])
    else:
        temp_string = "("

        if u_index < len(p):
            temp_string += dfs(p[u_index:])

        temp_string += ")"

        for u_p in p[:u_index][1 : u_index - 1]:
            if u_p == "(":
                temp_string += ")"
            else:
                temp_string += "("

    return temp_string


def solution(p):
    answer = ""

    if p:
        answer = dfs(p)

    return answer
