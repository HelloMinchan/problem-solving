import sys
input = sys.stdin.readline

x = []
y = []

for _ in range(3):
    a, b = input().split()
    (x.remove(a) if x.count(a) == 1 else x.append(a))
    (y.remove(b) if y.count(b) == 1 else y.append(b))

print(f'{x[0]+" "+y[0]}')