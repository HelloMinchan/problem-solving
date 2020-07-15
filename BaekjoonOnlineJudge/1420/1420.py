from collections import defaultdict, deque
import sys
input = sys.stdin.readline

MAX_N = 20002
INF = 2147483647

N, M = map(int, input().split())
city = [list(input().rstrip()) for _ in range(N)]
adjList = [[] for _ in range(MAX_N)]

capacity = defaultdict(lambda: defaultdict(int))
flow = defaultdict(lambda: defaultdict(int))

S = -1
T = -1
cnt = 0
sx = sy = tx = ty = 0

for i in range(N):
    for j in range(M):
        if city[i][j] == 'K':
            S = cnt + 1
            sx = j
            sy = i
        elif city[i][j] == 'H':
            T = cnt
            tx = j
            ty = i
        
        cnt += 2

if (N == 1 and M == 1) or S == -1 or T == -1 or abs(sx - tx) + abs(sy - ty) == 1:
    print(-1)
    sys.exit(0)

for i in range(N * M):
    capacity[2 * i][2 * i + 1] = 1
    adjList[2 * i].append(2 * i + 1)

    capacity[2 * i + 1][2 * i] = 0
    adjList[2 * i + 1].append(2 * i)

sv = 0;
for i in range(N):
    for j in range(M):
        if j + 1 < M and city[i][j] != '#' and city[i][j + 1] != '#':
            dv = sv + 2;

            capacity[sv + 1][dv] = INF;
            capacity[dv][sv + 1] = 0;

            capacity[dv + 1][sv] = INF;
            capacity[sv][dv + 1] = 0;

            adjList[sv + 1].append(dv);
            adjList[dv].append(sv + 1);

            adjList[dv + 1].append(sv);
            adjList[sv].append(dv + 1);

        if i + 1 < N and city[i][j] != '#' and city[i + 1][j] != '#':
            dv = 2 * M + sv;

            capacity[sv + 1][dv] = INF;
            capacity[dv][sv + 1] = 0;

            capacity[dv + 1][sv] = INF;
            capacity[sv][dv + 1] = 0;

            adjList[sv + 1].append(dv);
            adjList[dv].append(sv + 1);

            adjList[dv + 1].append(sv);
            adjList[sv].append(dv + 1);

        sv += 2;

totalFlow = 0

while 1:
    visit = [-1] * MAX_N

    dq = deque()
    visit[S] = True
    dq.append(S)

    while dq:
        sv = dq.popleft()
        
        for dv in adjList[sv]:
            if capacity[sv][dv] - flow[sv][dv] > 0 and visit[dv] == -1:
                visit[dv] = sv
                dq.append(dv)

                if dv == T:
                    break
    
    if visit[T] == -1:
        break

    i = T
    while i != S:
        flow[visit[i]][i] += 1
        flow[i][visit[i]] -= 1
        i = visit[i]
    
    totalFlow += 1

print(totalFlow)
