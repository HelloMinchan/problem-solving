import sys
input = sys.stdin.readline


def find(target):
    if ep[target] == target:
        return target
    
    center = find(ep[target])
    conLength[target] += conLength[ep[target]]
    ep[target] = center

    return ep[target]


def union(ep1, ep2):
    ep[ep1] = ep2
    conLength[ep1] = abs(ep1 - ep2) % 1000


T = int(input())

for _ in range(T):
    N = int(input())

    ep = list(range(N + 1))
    conLength = [0] * (N + 1)

    while 1:
        order = input().split()
        
        if order[0] == 'O':
            break
        
        if order[0] == 'E':
            target = int(order[1])
            find(target)
            print(conLength[target])
        elif order[0] == 'I':
            union(int(order[1]), int(order[2]))
