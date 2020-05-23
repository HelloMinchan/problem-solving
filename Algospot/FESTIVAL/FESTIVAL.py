import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    N, L = map(int, input().split())
    dailyCost = list(map(int, input().split()))
    minRentCost = 987654321.0

    for i in range(N - L + 1):
        day = 1
        rentCost = 0
        for j in range(i, N):
            rentCost += dailyCost[j]

            if day >= L:
                if minRentCost > rentCost / day:
                    minRentCost = rentCost / day

            day += 1

    print("%.8f" % minRentCost)