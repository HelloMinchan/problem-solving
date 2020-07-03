from collections import deque


def solution(operations):
    dq = deque()

    for oper in operations:
        o = oper.split()

        if o[0] == 'I':
            dq.append(int(o[1]))
        else:
            if dq:
                if o[1] == '1':
                    dq.pop()
                else:
                    dq.popleft()

        dq = deque(sorted(list(dq)))

    if dq:
        return [dq[-1], dq[0]]
    return [0, 0]from collections import deque


def solution(operations):
    dq = deque()

    for oper in operations:
        o = oper.split()

        if o[0] == 'I':
            dq.append(int(o[1]))
        else:
            if dq:
                if o[1] == '1':
                    dq.pop()
                else:
                    dq.popleft()

        dq = deque(sorted(list(dq)))

    if dq:
        return [dq[-1], dq[0]]
    return [0, 0]
