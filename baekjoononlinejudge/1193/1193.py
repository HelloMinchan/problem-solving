import sys
input = sys.stdin.readline

X = int(input())

temp = 0
i = 1

while X > temp:
    temp += i
    i += 1

i -= 1
diff = temp - X

if not i % 2:
    print(f"{i - diff}/{1 + diff}")
else:
    print(f"{1 + diff}/{i - diff}")