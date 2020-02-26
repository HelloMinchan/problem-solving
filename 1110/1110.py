import sys
input = sys.stdin.readline

a = int(input())
temp = a
cycle = 1

while True:
    temp = int(temp)
    if temp < 10:
        temp = str(temp)
        temp = '0' + temp
    temp = str(temp)
    temp2 = int(temp[0]) + int(temp[1])
    
    temp = str(temp)[1] + str(temp2)[-1]
    if int(temp) == a:
        break
    else:
        cycle += 1

print(cycle)