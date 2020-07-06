import sys
input = sys.stdin.readline


def failFunc(string):
    j = 0

    for i in range(1, len(string)):
        while j > 0 and string[i] != string[j]:
            j = table[j - 1]
        
        if string[i] == string[j]:
            j += 1
            table[i] = j


def KMP(T, P):
    global count

    j = 0
    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = table[j - 1]
            
        if T[i] == P[j]:
            if j == len(P) - 1:
                count += 1
                location.append(i - len(P) + 2)
                j = table[j]
            else:
                j += 1


T = input().rstrip()
P = input().rstrip()

table = [0] * len(T)
failFunc(P)

count = 0
location = []

KMP(T, P)

print(count)
print(*location)
