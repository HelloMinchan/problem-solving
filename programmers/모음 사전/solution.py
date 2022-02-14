def dfs(word):
    global answer, stack, spells
    answer += 1

    if "".join(stack) == word:
        return True
    if len(stack) == 5:
        return False

    for spell in spells:
        stack.append(spell)
        if dfs(word):
            return True
        stack.pop()


def solution(word):
    global answer, stack, spells

    answer = -1
    stack = []

    spells = ["A", "E", "I", "O", "U"]

    dfs(word)

    return answer