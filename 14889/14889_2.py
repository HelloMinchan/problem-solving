import sys
input = sys.stdin.readline
from itertools import combinations as C, permutations as P

people = [x for x in range(int(input()))]
S = [list(map(int, input().split())) for x in range(len(people))]
team = list(C(people, len(people) // 2))

limit = len(team)
gap = 9001
for i in range(limit // 2):
    sum1 = 0
    sum2 = 0
    startTeam = list(P(team[i], 2))
    linkTeam = list(P(team[limit - i - 1], 2))
    for j in range(len(startTeam)):
        sum1 += S[startTeam[j][0]][startTeam[j][1]]
        sum2 += S[linkTeam[j][0]][linkTeam[j][1]]
    if gap > abs(sum1 - sum2):
        gap = abs(sum1 - sum2)

print(gap)