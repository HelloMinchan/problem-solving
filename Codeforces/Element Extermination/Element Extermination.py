from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    seq = list(map(int, input().split()))
    
    print("YES" if seq[0] < seq[-1] else "NO")
