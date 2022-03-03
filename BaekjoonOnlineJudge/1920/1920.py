from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

number_dict = defaultdict(bool)

for number in A:
    number_dict[number] = True

M = int(input())
targets = list(map(int,input().split()))

for target in targets:
    print(1 if number_dict[target] else 0)