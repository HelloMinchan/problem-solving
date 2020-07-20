import sys
input = sys.stdin.readline


def cw(p1, p2):
    return p2[0] - p1[0], p2[1] - p1[1]

 
def ccw(p1, p2, p3):
    v1, v2 = cw(p1, p2), cw(p2, p3)
    
    if v1[0] * v2[1] > v1[1] * v2[0]:
        return True
    return False


def convexHull(coords):
    convex = []

    for p3 in coords:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]

            if ccw(p1, p2, p3):
                break

            convex.pop()
        convex.append(p3)
    print(len(convex))
    return len(convex)


N = int(input())
coords = [list(map(int, input().split())) for _ in range(N)]
answer = -2

coords.sort(key=lambda x:(x[0], x[1]))
answer += convexHull(coords)

coords.reverse()
answer += convexHull(coords)
print(answer)
