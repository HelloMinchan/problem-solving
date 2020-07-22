import sys
input = sys.stdin.readline

N = int(input())
lylics = ["baby", "sukhwan", 2, 1, "very", "cute", 2, 1, "in", "bed", 2, 1, "baby", "sukhwan"]

count = 0
for _ in range(N):
    count += 1
    if count >= 14:
        lylics[2] += 1
        lylics[3] += 1
        lylics[6] += 1
        lylics[7] += 1
        lylics[10] += 1
        lylics[11] += 1
        count = 0

if str(lylics[count - 1]).isdecimal():
    if lylics[count - 1] >= 5:
        print("tu+ru*%d" % lylics[count - 1])
    else:
        print("tu" + "ru"*lylics[count - 1])
else:
    print(lylics[count - 1])
