import sys
input = sys.stdin.readline

while True:
    side = list(map(int, input().split()))
    if not sum(side):
        break
    
    hypotenuse = max(side)
    side.remove(hypotenuse)

    print("right" if hypotenuse ** 2 == side[0] ** 2 + side[1] ** 2 else "wrong")