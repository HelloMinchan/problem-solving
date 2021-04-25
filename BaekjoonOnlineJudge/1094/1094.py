import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cheapest_package_price = 1001
cheapest_piece_price = 1001

for _ in range(M):
    package_price, piece_price = map(int,input().split())

    cheapest_package_price = min(cheapest_package_price, package_price)
    cheapest_piece_price = min(cheapest_piece_price, piece_price)

answer = 0

if cheapest_package_price / 6 < cheapest_piece_price:
    while N >= 6:
        N -= 6
        answer += cheapest_package_price

    if cheapest_package_price < cheapest_piece_price * N:
        answer += cheapest_package_price
    else:
        answer += cheapest_piece_price * N
else:
    answer = N * cheapest_piece_price

print(answer)
