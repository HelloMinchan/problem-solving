from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
zeroDurabilityCount = 0
# 0 : 내구도, 1 : 로봇 유무
conveyorBelt = deque(map(lambda durability: [durability, 0], A))

stageCount = 1

while 1:
    # 1단계
    conveyorBelt.rotate(1)
    conveyorBelt[N - 1][1] = 0

    # 2단계
    for beltIndex in range(N - 2, -1, -1):
        if (
            conveyorBelt[beltIndex][1] == 1
            and conveyorBelt[beltIndex + 1][1] == 0
            and conveyorBelt[beltIndex + 1][0] > 0
        ):
            # 로봇 이동
            conveyorBelt[beltIndex + 1][1] = 1
            conveyorBelt[beltIndex][1] = 0

            # 내구도 감소
            conveyorBelt[beltIndex + 1][0] -= 1
            if not conveyorBelt[beltIndex + 1][0]:
                zeroDurabilityCount += 1

    conveyorBelt[N - 1][1] = 0

    # 3단계
    if conveyorBelt[0][0] > 0 and conveyorBelt[0][1] == 0:
        # 로봇 투입
        conveyorBelt[0][1] = 1

        # 내구도 감소
        conveyorBelt[0][0] -= 1
        if not conveyorBelt[0][0]:
            zeroDurabilityCount += 1

    # 4단계
    if zeroDurabilityCount >= K:
        print(stageCount)
        break

    stageCount += 1