import sys, heapq
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

maxNum = max(A)
minNum = min(A)

heapq.heapify(A)

answer = maxNum - minNum

while 1:
    tempA = heapq.heappop(A)
    tempB = heapq.heappop(A)

    tempA += tempB

    maxNum = max(maxNum, tempA)

    heapq.heappush(A, tempA)
    heapq.heappush(A, tempB)
    
    if answer > maxNum - A[0]:
        answer = maxNum - A[0]
    else:
        break

print(answer)
