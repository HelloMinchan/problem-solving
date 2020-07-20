import sys
input = sys.stdin.readline

string = input().rstrip()

target = ['U', 'C', 'P', 'C']
count = 0

for s in string:
    if s == target[count]:
        count += 1

    if count == 4:
        break

if count == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")
