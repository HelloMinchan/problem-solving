import sys
input = sys.stdin.readline

for i in range(int(input())):
    arr = list(map(int, input().split()))
    num = arr[0]
    del arr[0]
    print('{:.3f}%'.format(len([x for x in arr if x > sum(arr) / len(arr)]) / len(arr) * 100))