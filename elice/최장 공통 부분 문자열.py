import sys

input = sys.stdin.readline

string1, string2 = list(input().split())

answer = 0
dp_table = [[0 for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]

for i in range(1, len(string1)+1):
    for j in range(1, len(string2)+1):
        if string1[i-1] == string2[j-1]:
            dp_table[i][j] = dp_table[i-1][j-1] + 1
            if answer < dp_table[i][j]:
                answer = dp_table[i][j]

print(answer)