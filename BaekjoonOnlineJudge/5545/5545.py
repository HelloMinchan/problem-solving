from math import floor
import sys

input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
C = int(input())
kal_of_toppings = sorted([int(input()) for _ in range(N)], reverse=True)

now_kal = C
now_price = A
best_pizza = now_kal / now_price

for kal_of_topping in kal_of_toppings:
    now_kal += kal_of_topping
    now_price += B

    if best_pizza < now_kal / now_price:
        best_pizza = now_kal / now_price
    else:
        break

print(floor(best_pizza))