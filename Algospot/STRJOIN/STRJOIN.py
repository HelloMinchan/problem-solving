import sys, heapq
input = sys.stdin.readline

c = int(input())

for _ in range(c):
    n = int(input().rstrip())
    strLength = []
    ans = 0

    for length in map(int, input().split()):
        heapq.heappush(strLength, length)
    
    for _ in range(n - 1):
        length1 = heapq.heappop(strLength)
        legnth2 = heapq.heappop(strLength)

        ans += length1 + legnth2
        heapq.heappush(strLength, length1 + legnth2)
    
    print(ans)