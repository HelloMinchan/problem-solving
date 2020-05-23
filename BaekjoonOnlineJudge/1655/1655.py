import sys, heapq
input = sys.stdin.readline

N = int(input())
middleValue = 0
smallHQ = []
smallHQCount = 0
bigHQ = []
bigHQCount = 0

for i in range(N):
    inputValue = int(input())

    if not i:
        middleValue = inputValue
        print(middleValue)
        continue
    
    if inputValue >= middleValue:
        heapq.heappush(smallHQ, (-middleValue, middleValue))
        smallHQCount += 1

        if not abs(smallHQCount - bigHQCount):
            heapq.heappush(bigHQ, (inputValue, -inputValue))
            middleValue = -heapq.heappop(bigHQ)[1]
            print(middleValue)
        elif abs(smallHQCount - bigHQCount) == 2:
            tempValue = heapq.heappop(smallHQ)[1]
            smallHQCount -= 1
            heapq.heappush(bigHQ, (inputValue, -inputValue))
            bigHQCount += 1
            heapq.heappush(bigHQ, (tempValue, -tempValue))
            middleValue = -heapq.heappop(bigHQ)[1]
            print(middleValue)
        else:
            print(middleValue)
            heapq.heappush(bigHQ, (inputValue, -inputValue))
            middleValue = -heapq.heappop(bigHQ)[1]
    else:
        heapq.heappush(bigHQ, (middleValue, -middleValue))
        bigHQCount += 1

        if not abs(smallHQCount - bigHQCount):
            heapq.heappush(smallHQ, (-inputValue, inputValue))
            middleValue = heapq.heappop(smallHQ)[1]
            print(middleValue)
        elif abs(smallHQCount - bigHQCount) == 2:
            tempValue = -heapq.heappop(bigHQ)[1]
            bigHQCount -= 1
            heapq.heappush(smallHQ, (-inputValue, inputValue))
            smallHQCount += 1
            heapq.heappush(smallHQ, (-tempValue, tempValue))
            middleValue = heapq.heappop(smallHQ)[1]
            print(middleValue)
        else:
            heapq.heappush(smallHQ, (-inputValue, inputValue))
            middleValue = heapq.heappop(smallHQ)[1]
            print(middleValue)