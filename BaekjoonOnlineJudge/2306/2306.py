import sys
input = sys.stdin.readline


def gFind(s, e):
    if s >= e:
        return 0

    length = 0

    for i in range(s, e):
        if DNA[i] == 'a' and DNA[e] == 't' or DNA[i] == 'g' and DNA[e] == 'c':
            memoization[i][e] = max(length, gFind(i + 1, e - 1) + 2 + gFind(e + 1, e))
        elif DNA[i] == 'a' and DNA[i] == 'g':
            memoization[i][e] = max(length, gFind(i + 1, e))
        length = max(length, gFind(s, e - 1))

    return length
    

DNA = input().rstrip()

memoization = [[0] * 501 for _ in range(501)]
        
print(gFind(0, len(DNA) - 1))
