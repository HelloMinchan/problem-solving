import sys
input = sys.stdin.readline

n = int(input())

temp = 0
i = 1

while n > temp:
    temp += i
    i += 1

i -= 1
diff = temp - n

if i % 2 == 0:
    print(f"{i - diff}/{1 + diff}")
else:
    print(f"{1 + diff}/{i - diff}")