import sys
input = sys.stdin.readline

tot = int(input())
for _ in range(tot):
    visit = [False] * 26
    word = list(input().rstrip())
    pre = word[0]
    for i in word:
        if visit[ord(i) - 97] == True:
            tot -= 1
            break
        else:
            if pre == i:
                pre = i
            else:
                visit[ord(pre) - 97] = True
                pre = i

print(tot)