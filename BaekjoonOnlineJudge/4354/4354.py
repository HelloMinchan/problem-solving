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


while 1:
    string = input().rstrip()

    if string == '.':
        break

    table = [0] * (len(string))
    failFunc(string)

    i = len(string) - 1
    while table[i]:
        i -= 1

    print(len(string) // (i + 1) if not len(string) % (i + 1) else 1)

