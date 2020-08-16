import sys
input = sys.stdin.readline

hash_arr = [0] * 10001
N = int(input())

for _ in range(N):
    hash_arr[int(input())] += 1

for i, num in enumerate(hash_arr):
    for _ in range(num):
        print(i)

