import sys
input = sys.stdin.readline

N = int(input())

memoization = [0] * (N + 1)

for i in range(1, N + 1):
    memoization[i] = i

    for j in range(1, N + 1):
        if j ** 2 > i:
            break
        if memoization[i] > memoization[i - j ** 2] + 1:
            memoization[i] = memoization[i - j ** 2] + 1
        
print(memoization[-1])
