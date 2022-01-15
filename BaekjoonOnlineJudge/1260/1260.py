from collections import deque as Deque
import sys
input = sys.stdin.readline

def initialize_visit_list(start_vertex):
    global N
    
    visit_list = [False for _ in range(N+1)]
    visit_list[start_vertex] = True

    return visit_list

def DFS(start_vertex):
    global stack

    for vertex in adjacent_list[start_vertex]:
        if not visit_list[vertex]:
            visit_list[vertex] = True
            stack.append(vertex)
            DFS(vertex)

def BFS(start_vertex):
    global deque
    answer = []

    while deque:
        start_vertex = deque.popleft()
        answer.append(start_vertex)

        for vertex in adjacent_list[start_vertex]:
            if not visit_list[vertex]:
                visit_list[vertex] = True
                deque.append(vertex)
    
    print(*answer)  


N, M, V = map(int, input().split())

adjacent_list = [[] for _ in range(N+1)]

for _ in range(M):
    start_vertex, destination_vertex = map(int, input().split())

    adjacent_list[start_vertex].append(destination_vertex)
    adjacent_list[start_vertex].sort()

    adjacent_list[destination_vertex].append(start_vertex)
    adjacent_list[destination_vertex].sort()

    

visit_list = initialize_visit_list(V)
stack = [V]
DFS(V)
print(*stack)

visit_list = initialize_visit_list(V)
deque = Deque([V])
BFS(V)