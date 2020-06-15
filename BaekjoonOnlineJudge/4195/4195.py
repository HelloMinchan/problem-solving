import sys
input = sys.stdin.readline


def find(target):
    if table[target] == target:
        return target

    table[target] = find(table[target])
    return table[target]


def union(f1, f2):
    foundF1 = find(f1)
    foundF2 = find(f2)

    if foundF1 == foundF2:
        return
    elif foundF1 < foundF2:
        count[foundF1] += count[foundF2]
        table[foundF2] = foundF1
    else:
        count[foundF2] += count[foundF1]
        table[foundF1] = foundF2


TC = int(input())

for _ in range(TC):
    F = int(input())

    table = dict()
    count = dict()

    for _ in range(F):
        ans = 0
        friendship = input().rstrip().split()
        
        for name in friendship:
            if not table.get(name, 0):
                table[name] = name
                count[name] = 1
        
        union(friendship[0], friendship[1])

        print(count[find(friendship[0])])
