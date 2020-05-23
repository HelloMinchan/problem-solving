arr = []
i = 0
while i <= 10000:
    arr.append(True)
    i += 1

i = 1
while i < 10000:
    if i < 10:
        arr[i + i] = False
    elif i >= 10 and i < 100:
        arr[i + int(str(i)[0]) + int(str(i)[1])] = False
    elif i >= 100 and i < 1000:
        arr[i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2])] = False
    else:
        temp = i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3])
        if temp <= 10000:
            arr[temp] = False
    i += 1

for i in range(1, len(arr)):
    if arr[i]:
        print(i)