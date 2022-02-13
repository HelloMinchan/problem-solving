# 9:55 ~

import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def dfs(now_vertex, flag):
    visit[now_vertex] = flag

    for vertex in adjacency_list[now_vertex]:
        if visit[vertex] == 0:
            answer = dfs(vertex, -flag)

            if answer == "NO":
                return answer
        elif visit[vertex] == flag:
            return "NO"

    return "YES"


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())

    adjacency_list = [[] for _ in range(V + 1)]
    visit = [0 for _ in range(V + 1)]

    for _ in range(E):
        sv, dv = map(int, input().split())

        adjacency_list[sv].append(dv)
        adjacency_list[dv].append(sv)

    for vertex in range(1, V + 1):
        if visit[vertex] == 0:
            if dfs(vertex, 1) == "NO":
                print("NO")
                break
    else:
        print("YES")