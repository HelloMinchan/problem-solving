def GCD(a, b):
    return b if not a % b else GCD(b, a % b)


def solution(n, m):
    gcd = GCD(n, m)
    lcm = n * m // gcd
    
    return [gcd, lcm]
