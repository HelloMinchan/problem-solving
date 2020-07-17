import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    seq = list(map(int, input().split()))
    count = dict()

    for num in seq:
        count[num] = count.get(num, 0) + 1
    
    comp = []
    for key, val in count.items():
        comp.append((key, val))
    
    comp.sort()

    if len(comp) == 1:
        print("YES")
        print(comp[0][0], comp[0][0], comp[0][0])
    elif len(comp) == 3:
        print("NO")
    else:
        if comp[0][1] > comp[1][1]:
            print("NO")
        else:
            print("YES")
            print(comp[1][0], comp[0][0], comp[0][0])
