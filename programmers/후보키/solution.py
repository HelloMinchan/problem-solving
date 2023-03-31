from collections import defaultdict


def is_candidate(relation, candidate):
    database = defaultdict(int)

    for row in relation:
        key = ""

        for i in candidate:
            key += row[i]

        if database[key] == 0:
            database[key] = 1
        else:
            return False

    return True


def dfs(start, relation):
    global answer, stack, visit, candidates

    if stack:
        candidates.append(stack[:])

    if len(stack) >= len(relation[0]):
        return

    for i in range(start, len(relation[0])):
        if not visit[i]:
            visit[i] = True
            stack.append(i)
            dfs(i + 1, relation)
            visit[i] = False
            stack.pop()


def is_subset(candidate, found_candidates):
    for found_candidate in found_candidates:
        if set(found_candidate).issubset(candidate):
            return True

    return False


def solution(relation):
    global answer, stack, visit, candidates

    answer = 0
    stack = []
    visit = [False for _ in range(len(relation[0]))]
    candidates = []

    dfs(0, relation)
    candidates.sort(key=lambda candidate: len(candidate))

    found_candidates = []

    for candidate in candidates:
        if is_candidate(relation, candidate) and not is_subset(
            candidate, found_candidates
        ):
            answer += 1
            found_candidates.append(set(candidate))

    return answer
