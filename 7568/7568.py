import sys
input = sys.stdin.readline

N = int(input())
person = []
for _ in range(N):
    w, h = map(int, input().split())
    person.append([w, h])

for i in range(N):
    count = 0
    for j in range(N):
        if i == j:
            continue
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            count += 1
    print(count + 1, "", end="")