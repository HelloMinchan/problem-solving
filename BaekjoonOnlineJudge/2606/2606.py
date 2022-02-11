import sys

input = sys.stdin.readline


def DFS(start_vertex):
    global answer
    answer += 1

    for vertex in adjacency_list[start_vertex]:
        if not visit[vertex]:
            visit[vertex] = True
            DFS(vertex)


answer = 0
computer_count = int(input())
edge = int(input())
adjacency_list = [[] for _ in range(computer_count + 1)]

for _ in range(edge):
    sv, dv = map(int, input().split())

    adjacency_list[sv].append(dv)
    adjacency_list[dv].append(sv)

visit = [False for _ in range(computer_count + 1)]
visit[1] = True

DFS(1)

print(answer - 1)
