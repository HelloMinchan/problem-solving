import sys
input = sys.stdin.readline

N, M = map(int, input().split())

adjList = [[] for _ in range(N)]

for i in range(N):
    temp = list(map(int, input().split()))
    
    for j in range(1, len(temp)):
        adjList[i].append(temp[j])

print(adjList)
