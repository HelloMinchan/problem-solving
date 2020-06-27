import sys
input = sys.stdin.readline


def find(target):
    if tops[target] == target:
        return target

    tops[target] = find(tops[target])
    return tops[target]


def union(t1, t2):
    findT1 = find(t1)
    findT2 = find(t2)

    if findT1 == findT2:
        return

    if findT1 < findT2:
        tops[findT2] = findT1
        mainTops[findT1] += mainTops[findT2]
        mainTops[findT2] = 0
    else:
        tops[findT1] = findT2
        mainTops[findT2] += mainTops[findT1]
        mainTops[findT1] = 0
    

N, M, Q = map(int, input().split())

conn = [[0, 0, 0]] + [list(map(int, input().split())) + [1] for _ in range(M)]
disConn = []
for _ in range(Q):
    v = int(input())
    disConn.append(v)
    conn[v][2] = 0

mainTops = [1] * (N + 1)
tops = list(range(N + 1))

for i in range(1, M + 1):
    if conn[i][2]:
        union(conn[i][0], conn[i][1])

cost = 0
while disConn:
    i = disConn.pop()
    t1 = conn[i][0]
    t2 = conn[i][1]
    
    if find(t1) != find(t2):
        cost += mainTops[find(t1)] * mainTops[find(t2)]

    union(t1, t2)

print(cost)
