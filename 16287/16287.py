import sys
input = sys.stdin.readline

w, n = map(int, input().split())
A = list(map(int, input().split()))
addA = []

for i in range(n):
    for j in range(i + 1, n):
        addA.append(A[i] + A[j])

addA = sorted(addA)

startPointer = 0
endPointer = 0
sumValue = 0

while(True):
    if sumValue >= w:
        sumValue -= A[startPointer]
        startPointer += 1
    elif endPointer == len(A):
        break
    else:
        sumValue += A[endPointer]
        endPointer += 1
    
    if sumValue == w and endPointer - startPointer == 4:
        print("YES")
        sys.exit(0)

print("NO")