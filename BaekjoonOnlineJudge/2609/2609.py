import sys
input = sys.stdin.readline


def GCD(a, b):
    return b if not a % b else GCD(b, a % b)


a, b = map(int, input().split())

gcd = GCD(a, b)

print(gcd)
print(a * b // gcd)
