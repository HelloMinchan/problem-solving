from math import gcd
import sys
input = sys.stdin.readline


def lcm(x, y):
    return x * y // gcd(x, y)


t = int(input())

for _ in range(t):
    n = int(input())

    left = 0
    right = 1000000000
    minLCM = 2147483647
    ans1 = 0
    ans2 = 0

    if n % 2:
        while left <= right:
            mid = (left + right) // 2

            another = n - mid

            if n - mid <= 0:
                right = mid - 1
            else:
                temp = lcm(mid, another)
                
                if minLCM > temp:
                    if mid == 0 or another == 0:
                        right = mid - 1
                        continue
                    minLCM = temp
                    ans1 = min(mid, another)
                    ans2 = max(mid, another)
                    right = mid - 1
                else:
                    left = mid + 1
        print(ans1, ans2)
    else:
        print(n // 2, n // 2)
    
