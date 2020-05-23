num = 0

for i in range(1, int(input()) + 1):
    if i < 100:
        num += 1
    else:
        i = str(i)
        if int(i[0]) - int(i[1]) == int(i[1]) - int(i[2]):
            num += 1

print(num)