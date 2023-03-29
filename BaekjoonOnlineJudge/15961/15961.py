from collections import defaultdict
import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(N)]
belt += belt[: k + 1]

answer = 0
left = 0
right = 1

sushi_type_dict = defaultdict(int)
sushi_type_dict[belt[left]] = 1
sushi_type_dict[c] = 1
sushi_count = 1

while right < len(belt):
    # 연속 횟수 초과 안했을 경우
    if sushi_count + 1 <= k:
        sushi_type_dict[belt[right]] += 1
        sushi_count += 1
    # 연속 횟수를 초과했을 경우
    else:
        # 버릴 스시가 하나밖에 없을 경우
        if sushi_type_dict[belt[left]] == 1:
            del sushi_type_dict[belt[left]]
        else:
            sushi_type_dict[belt[left]] -= 1
        left += 1

        sushi_type_dict[belt[right]] += 1

    right += 1
    answer = max(answer, len(sushi_type_dict.keys()))

print(answer)
