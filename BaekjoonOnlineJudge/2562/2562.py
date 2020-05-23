import sys, copy
input = sys.stdin.readline

arr = []
for i in range(9):
    arr.append(int(input()))

temp = copy.deepcopy(arr)
arr.sort()

print(arr[-1])
print(temp.index(arr[-1]) + 1)