import sys
input = sys.stdin.readline

N = int(input())
divisor = sorted(map(int, input().split()))

print(divisor[0] * divisor[-1])
