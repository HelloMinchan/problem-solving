N = int(input())
score = []
temp = input()
score = temp.split()
score = [int(x) for x in score]
score.sort()
print(score[N//2])
