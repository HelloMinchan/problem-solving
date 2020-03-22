# 유클리드 호제법 적용
import sys
input = sys.stdin.readline


def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


a, b = map(int, input().split())
g = gcd(a, b)
print(g, a * b // g, sep="\n")

# 유클리드 호제법 미적용
# import sys
# input = sys.stdin.readline

# a, b = map(int, input().split())

# for i in range(b, 0, -1):
#     if a % i == 0 and b % i == 0:
#         print(i)
#         print(i * a // i * b // i)
#         exit()