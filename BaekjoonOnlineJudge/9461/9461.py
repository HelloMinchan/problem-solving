import sys

input = sys.stdin.readline

T = int(input())
dp_table = [0 for _ in range(101)]
dp_table[1] = 1
dp_table[2] = 1
dp_table[3] = 1
dp_table[4] = 2
dp_table[5] = 2

for _ in range(T):
    N = int(input())

    for i in range(6, N+1):
        dp_table[i] = dp_table[i-1] + dp_table[i-5]
    
    print(dp_table[N])
