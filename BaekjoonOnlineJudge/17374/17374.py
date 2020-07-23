import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    bit, berry, A, B, C, D = map(int, input().split())
    # 비트, 코인, 베리, 비트코인
    wallet = [bit, 0, berry, 0]

    while 1:
        # 비트코인 만들기
        while wallet[0] and wallet[1]:
            wallet[3] += 1
            wallet[0] -= 1
            wallet[1] -= 1
        # 비트가 코인보다 많을 때 (코인을 만들자)
        if wallet[0] > wallet[1]:
            if wallet[2] >= C:
                wallet[2] -= C
                wallet[1] += D
            elif wallet[0] > A:
                wallet[0] -= A
                wallet[1] += B
            else:
                break
        # 코인이 비트보다 많을 때 (비트를 만들자)
        elif wallet[0] < wallet[1]:
            if wallet[1] > B:
                wallet[0] -= B
                wallet[1] += A
            else:
                if wallet[1] > D:
                    wallet[1] -= D
                    wallet[2] += C
                else:
                    break
        else:
            break

    print(wallet[3])
