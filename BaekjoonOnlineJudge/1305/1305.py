import sys
input = sys.stdin.readline


def failFunc(string):
    j = 0

    for i in range(1, L):
        while j > 0 and string[i] != string[j]:
            j = failTable[j - 1]
        
        if string[i] == string[j]:
            j += 1
            failTable[i] = j


L = int(input())
string = input().rstrip()

failTable = [0] * L

failFunc(string)

print(L - failTable[L - 1])
