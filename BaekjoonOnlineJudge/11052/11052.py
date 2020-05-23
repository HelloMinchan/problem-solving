# PyPy3 정답, Python 3 시간 초과
import sys
input = sys.stdin.readline

N = int(input())
prices = [0] + list(map(int, input().split()))
memoiztaion = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, i + 1):
        memoiztaion[i][j] = prices[j] + max(memoiztaion[i - j])
        
print(max(memoiztaion[-1]))