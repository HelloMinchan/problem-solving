import sys
input = sys.stdin.readline


def gFind(s, e):
    if s >= e:
        return 0

    if memoization[s][e] != -1:
        return memoization[s][e]

    for i in range(s, e + 1):
        if (DNA[s] == 'a' and DNA[i] == 't') or (DNA[s] == 'g' and DNA[i] == 'c'):
            memoization[s][e] = max(memoization[s][e], gFind(s + 1, i - 1) + 2 + gFind(i + 1, e))
        memoization[s][e] = max(memoization[s][e], gFind(s + 1, i) + gFind(i + 1, e))
        
    return memoization[s][e]
    

DNA = input().rstrip()

memoization = [[-1] * 501 for _ in range(501)]
        
print(gFind(0, len(DNA) - 1))
