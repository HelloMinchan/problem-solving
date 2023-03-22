import sys

input = sys.stdin.readline

N, M, T, K = map(int, input().split())

obsidian_position = []
for _ in range(T):
    x, y = map(int, input().split())
    obsidian_position.append((x, y))

answer_x = 0
answer_y = 0
answer_count = 0

for i in range(T):
    base_obsidian = obsidian_position[i]

    for j in range(T):
        # 좌 하단 꼭짓점 좌표
        target_x = 0
        target_y = 0

        compare_obsidian = obsidian_position[j]

        # 사각형 X크기 결정 (N초과 방지)
        if base_obsidian[0] + K > N:
            target_x = N - K
        else:
            target_x = base_obsidian[0]

        # 사각형 Y크기 결정 (N초과 방지)
        if compare_obsidian[1] + K > M:
            target_y = M - K
        else:
            target_y = compare_obsidian[1]

        obsidian_count = 0
        for obsidian_x, obsidian_y in obsidian_position:
            if (
                target_x <= obsidian_x <= target_x + K
                and target_y <= obsidian_y <= target_y + K
            ):
                obsidian_count += 1

        if answer_count < obsidian_count:
            answer_count = obsidian_count
            answer_x = target_x
            answer_y = target_y + K

print(answer_x, answer_y)
print(answer_count)
