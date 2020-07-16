import sys
input = sys.stdin.readline


def GCD(a, b):
    return b if not a % b else GCD(b, a % b)


N = int(input())

colonade = [int(input()) for _ in range(N)]
colonade.sort()

dist = []
for i in range(1, N):
    dist.append(colonade[i] - colonade[i - 1])

gcd = GCD(dist[0], dist[1])

answer = 0
for d in dist:
    answer += d // gcd - 1

print(answer)
