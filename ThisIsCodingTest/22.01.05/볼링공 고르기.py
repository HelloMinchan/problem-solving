import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bowlings = list(map(int, input().split()))

print(sum(range(1, N)) - (len(bowlings) - len(set(bowlings))))