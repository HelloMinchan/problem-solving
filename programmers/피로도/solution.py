def dfs(clear, k, dungeons):
    global visit, answer, stack

    if answer < clear:
        answer = clear

    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visit[i]:
            k -= dungeons[i][1]
            visit[i] = True
            stack.append(i)
            dfs(clear + 1, k, dungeons)
            stack.pop()
            k += dungeons[i][1]
            visit[i] = False


def solution(k, dungeons):
    global visit, answer, stack

    stack = []
    answer = -1
    visit = [False for _ in range(len(dungeons))]

    dfs(0, k, dungeons)

    return answer