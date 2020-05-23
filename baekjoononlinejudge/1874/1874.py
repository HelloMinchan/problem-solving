import sys
input = sys.stdin.readline

exm = []
temp = []
answer = []
t = int(input())
for _ in range(1, t + 1):
    exm.append(int(input()))

cur = 0
i = 1
while True:
    if i == t + 1:
        break;
    if i != exm[cur]:
        temp.append(i)
        answer.append('+')
        i += 1
    if len(temp) != 0:
        if temp[-1] == exm[cur]:
            temp.pop()
            answer.append('-')
            cur += 1
            i -= 1
    