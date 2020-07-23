import sys
input = sys.stdin.readline


def makeOrder(target, start, end):
    if start == end:
        if target:
            print('#', end="")
        else:
            print('.', end="")
        return
    
    length = end - start + 1

    if target <= length // 2:
        makeOrder(target, start, ((start + end) >> 1))
        makeOrder(0, ((start + end) >> 1) + 1, end)
    else:
        mid = ((start + end) >> 1)
        double = 1
        while double * 2 <= target - double * 2 and double * 2 <= end - mid:
            double = double * 2
        if target - double > mid - start + 1:
            double = target - (mid - start + 1)
            
        makeOrder(target - double, start, mid)
        makeOrder(double, mid + 1, end)


N = int(input())
slot = 1
while 1:
    if slot < N: slot <<= 1
    else: break

makeOrder(N, 1, slot)
