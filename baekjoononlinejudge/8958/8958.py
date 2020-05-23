import sys
input = sys.stdin.readline

for i in range(int(input())):
    totScore = 0
    score = 1
    arr = list(input())
    for j in arr:
        if(j == 'O'):
            totScore += score
            score += 1
        else:
            score = 1
    print(totScore)